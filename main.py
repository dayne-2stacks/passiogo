from fastapi import FastAPI
import passiogo 

app = FastAPI()

system = passiogo.getSystemFromID(2343)

routes_obj = [route for route in system.getRoutes()]

routes ={}
for route in system.getRoutes():
    print(route)
    routes[route.__dict__["id"]] = (route.__dict__) 

stops = {} 
for stop in system.getStops():
    stops[stop.__dict__["id"]]= stop.__dict__

@app.get("/routes")
def get_routes():
    return routes

@app.get("/routes/{route_id}")
def get_route(route_id: str):
    return routes[route_id]

@app.get("/stops")
def get_stops():
    return stops

@app.get("/routes/{route_id}/stops")
def get_route_stops(route_id: str):
    for i in range(len(routes_obj)):
        if routes_obj[i].__dict__['id']==route_id:
            route_stops={}
            for stop in routes_obj[i].getStops():
                route_stops[stop.__dict__['id']]= stop.__dict__

            return route_stops

@app.get("stops/{stop_id}")
def get_stop(stop_id: str):
    return stops[stop_id]

if __name__ == "__main__":
    a = get_route_stops('70692')
    print(a)
