import requests, json
from flask import Flask, render_template

def get_stasjoner_fra_api():
    #request informasjon
    request_url = "https://gbfs.urbansharing.com/oslobysykkel.no/station_information.json"
    request_header = {'Client-Identifier': 'origo-ledigbysykler'}

    try:
        # Sender request og henter info stasjoners addresse og navn
        request = requests.get(request_url, headers=request_header) # try-except
        request.raise_for_status()
        response = request.text
        
        # Laster inn informasjonen
        data = json.loads(response)
        return data

    except requests.exceptions.RequestException:
        return None # Kan haandtere feilmeldinger relatert til request 
    except json.JSONDecodeError:
        return None # Kan haandtere feilmeldinger relatert til json
    except Exception:
        return None # Kan haandtere generelle feilmeldinger som oppstaar
    
def get_ledige_stasjoner_fra_api(): # liknende try-except trenges her ogsaa

    #request informasjon
    request_url = "https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json"
    request_header = {'Client-Identifier': 'origo-ledigbysykler'}
    
    try:
        # Sender request og henter info stasjoners addresse og navn
        request = requests.get(request_url, headers=request_header)
        request.raise_for_status()
        response = request.text
        
        # Laster inn informasjonen
        data = json.loads(response)
        return data

    except requests.exceptions.RequestException:
        return None # Kan haandtere feilmeldinger relatert til request 
    except json.JSONDecodeError:
        return None # Kan haandtere feilmeldinger relatert til json
    except Exception:
        return None # Kan haandtere generelle feilmeldinger som oppstaar 

def get_stasjon_informasjon():
    stasjoner = get_stasjoner_fra_api()
    ledige_stasjoner = get_ledige_stasjoner_fra_api()

    samlet_stasjon_informasjon = []

    for stasjon in stasjoner['data']['stations']:
        # Omgjoor string til int
        stasjon_id = -1
        try:
            stasjon_id = int(stasjon['station_id'])
        except Exception:
            continue # Ugyldig id, gaar videre til neste iterasjon.

        obj = {
            'station_id': stasjon_id,
            'name': stasjon['name'],
            # 'address': stasjon['address'],
            # 'capacity': stasjon['capacity'],
            # 'lat': stasjon['lat'],
            # 'lon': stasjon['lon'],
            'num_bikes_available': 0,
            'num_docks_available': 0,
        }
        for ledige_stasjon in ledige_stasjoner['data']['stations']:

            # Omgjoor string til int
            ledig_stasjon_id = -1
            try:
                ledig_stasjon_id = int(ledige_stasjon['station_id'])
            except Exception:
                continue # Ugyldig id, gaar videre til neste iterasjon
            
            # Dersom de to endepunktenes "station_id" er like settes antallet ledige sykkler og tilgjengelige laaser
            if stasjon_id == ledig_stasjon_id:
                obj['num_bikes_available'] = ledige_stasjon['num_bikes_available'],
                obj['num_docks_available'] = ledige_stasjon['num_docks_available'],
        
        samlet_stasjon_informasjon.append(obj)

    return samlet_stasjon_informasjon


# Setter opp Flask
app = Flask(__name__)

# Hoved endepunkt for nettsiden
@app.get("/")
def index():
    # Laster inn index.html filen
    return render_template("index.html")

# Returnere informasjon som navnet paa stasjonen, tilgjengelige sykkler og ledige laaser, gjennom endepunktet "/info/"
@app.get("/info/")
def stasjon_informasjon():
    return get_stasjon_informasjon()
