import { useEffect, useState } from 'react'
import {
  MapContainer,
  TileLayer,
  Marker,
  Popup,
  Polyline,
  useMap,
} from 'react-leaflet'
import 'leaflet/dist/leaflet.css'

import { getLiveFleet, getRoute } from '../../services/api'

function RecenterMap({ position }) {
  const map = useMap()

  useEffect(() => {
    if (position) {
      map.setView(position, map.getZoom(), {
        animate: true,
      })
    }
  }, [position, map])

  return null
}

const LiveMap = () => {
  const [vehicles, setVehicles] = useState([])
  const [route, setRoute] = useState([])

  async function loadVehicles() {
    try {
      const data = await getLiveFleet()
      setVehicles(data)
    } catch (err) {
      console.error(err)
    }
  }

  async function loadRoute() {
    try {
      const data = await getRoute('R001')
      setRoute(data.waypoints)
    } catch (err) {
      console.error(err)
    }
  }

  useEffect(() => {
    loadVehicles()
    loadRoute()

    const interval = setInterval(loadVehicles, 2000)

    return () => clearInterval(interval)
  }, [])

  const center =
    vehicles.length > 0
      ? [vehicles[0].latitude, vehicles[0].longitude]
      : [18.5204, 73.8567]

  return (
    <MapContainer center={center} zoom={13} style={{ height: '80vh', width: '100%' }}>
      <TileLayer
        attribution="&copy; OpenStreetMap contributors"
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />

      <RecenterMap position={center} />

      {route.length > 0 && (
        <Polyline
          positions={route}
          pathOptions={{
            color: 'blue',
            weight: 5,
          }}
        />
      )}

      {vehicles.map((vehicle) => (
        <Marker
          key={vehicle.vehicle_id}
          position={[vehicle.latitude, vehicle.longitude]}
        >
          <Popup>
            <strong>{vehicle.vehicle_id}</strong>

            <br />
            Driver: {vehicle.driver_id}

            <br />
            Speed: {vehicle.speed} km/h

            <br />
            Fuel: {Number(vehicle.fuel_level).toFixed(1)}%

            <br />
            Remaining: {Number(vehicle.remaining_distance_km).toFixed(1)} km

            <br />
            ETA: {Math.round(vehicle.eta_minutes)} min
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  )
}

export default LiveMap
