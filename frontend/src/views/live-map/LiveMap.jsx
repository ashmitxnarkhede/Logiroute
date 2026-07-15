import { useEffect, useState } from 'react'
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import 'leaflet/dist/leaflet.css'

import { getLiveFleet } from '../../services/api'

const LiveMap = () => {
  const [vehicle, setVehicle] = useState(null)

  useEffect(() => {
    loadVehicle()

    const interval = setInterval(loadVehicle, 2000)

    return () => clearInterval(interval)
  }, [])

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

  return (
    <MapContainer center={[18.5204, 73.8567]} zoom={7} style={{ height: '80vh', width: '100%' }}>
      <TileLayer
        attribution="&copy; OpenStreetMap contributors"
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />

      {vehicle && (
        <Marker position={[vehicle.latitude, vehicle.longitude]}>
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
