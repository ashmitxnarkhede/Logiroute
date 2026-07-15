import { useEffect, useState } from 'react'
import { getLiveFleet } from '../../services/api'

const Dashboard = () => {
  const [vehicles, setVehicles] = useState([])

  useEffect(() => {
    loadData()

    const interval = setInterval(loadData, 2000)

    return () => clearInterval(interval)
  }, [])

  async function loadData() {
    try {
      const data = await getLiveFleet()
      setVehicles(data)
    } catch (err) {
      console.error(err)
    }
  }

  return (
    <div className="container-fluid">
      <h2>LogiRoute Dashboard</h2>

      <table className="table table-striped">
        <thead>
          <tr>
            <th>Vehicle</th>
            <th>Speed</th>
            <th>Fuel</th>
            <th>Latitude</th>
            <th>Longitude</th>
          </tr>
        </thead>

        <tbody>
          {vehicles.map((v, index) => (
            <tr key={index}>
              <td>{v.vehicle_id}</td>
              <td>{v.speed}</td>
              <td>{Number(v.fuel_level).toFixed(1)}%</td>
              <td>{v.latitude.toFixed(5)}</td>
              <td>{v.longitude.toFixed(5)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default Dashboard
