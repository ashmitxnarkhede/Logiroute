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
  const [vehicle, setVehicle] = useState(null)
  const [route, setRoute] = useState([])

  async function loadVehicle() {
    try {
      const data = await getLiveFleet()

      if (data.length > 0) {
        setVehicle(data[0])
      }
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
    loadVehicle()
    loadRoute()

    const interval = setInterval(loadVehicle, 2000)

    return () => clearInterval(interval)
  }, [])

  const position = vehicle ? [vehicle.latitude, vehicle.longitude] : [18.5204, 73.8567]

  return (
    <MapContainer center={position} zoom={13} style={{ height: '80vh', width: '100%' }}>
      <TileLayer
        attribution="&copy; OpenStreetMap contributors"
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />

      <RecenterMap position={position} />

      {route.length > 0 && (
        <Polyline
          positions={route}
          pathOptions={{
            color: 'blue',
            weight: 5,
          }}
        />
      )}

      {vehicle && (
        <Marker position={position}>
          <Popup>
            <strong>{vehicle.vehicle_id}</strong>
            <br />
            Speed: {vehicle.speed} km/h
            <br />
            Fuel: {vehicle.fuel_level.toFixed(1)}%
          </Popup>
        </Marker>
      )}
    </MapContainer>
  )
}

export default LiveMap
