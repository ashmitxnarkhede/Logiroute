import { useEffect, useState } from 'react'
import { getLiveFleet } from '../../services/api'

const Dashboard = () => {
  const [vehicles, setVehicles] = useState([])
  const [search, setSearch] = useState('')

  const activeVehicles = vehicles.filter((v) => v.status === 'MOVING').length

  const averageSpeed =
    vehicles.length > 0
      ? (vehicles.reduce((sum, v) => sum + Number(v.speed), 0) / vehicles.length).toFixed(1)
      : 0

  const averageFuel =
    vehicles.length > 0
      ? (
          vehicles.reduce((sum, v) => sum + Number(v.fuel_level), 0) / vehicles.length
        ).toFixed(1)
      : 0

  const averageETA =
    vehicles.length > 0
      ? (
          vehicles.reduce((sum, v) => sum + Number(v.eta_minutes), 0) / vehicles.length
        ).toFixed(0)
      : 0

  const filteredVehicles = vehicles.filter((v) =>
    v.vehicle_id.toLowerCase().includes(search.toLowerCase())
  )

  async function loadData() {
    try {
      const data = await getLiveFleet()
      setVehicles(data)
    } catch (err) {
      console.error(err)
    }
  }

  const alerts = []

  vehicles.forEach((v) => {
    if (v.fuel_level < 20) {
      alerts.push({
        type: 'warning',
        message: `${v.vehicle_id} has low fuel (${Number(v.fuel_level).toFixed(1)}%)`,
      })
    }

    if (v.speed > 70) {
      alerts.push({
        type: 'danger',
        message: `${v.vehicle_id} is overspeeding (${v.speed} km/h)`,
      })
    }

    if (v.status === 'ARRIVED') {
      alerts.push({
        type: 'success',
        message: `${v.vehicle_id} has reached its destination`,
      })
    }
  })

  useEffect(() => {
    loadData()

    const interval = setInterval(loadData, 2000)

    return () => clearInterval(interval)
  }, [])

  return (
    <div className="container-fluid">
      <h2>LogiRoute Dashboard</h2>

      <div className="row mb-4">
        <div className="col-md-3">
          <div className="card text-bg-primary">
            <div className="card-body">
              <h6>Active Vehicles</h6>
              <h2>{activeVehicles}</h2>
            </div>
          </div>
        </div>

        <div className="col-md-3">
          <div className="card text-bg-success">
            <div className="card-body">
              <h6>Average Speed</h6>
              <h2>{averageSpeed} km/h</h2>
            </div>
          </div>
        </div>

        <div className="col-md-3">
          <div className="card text-bg-warning">
            <div className="card-body">
              <h6>Average Fuel</h6>
              <h2>{averageFuel}%</h2>
            </div>
          </div>
        </div>

        <div className="col-md-3">
          <div className="card text-bg-danger">
            <div className="card-body">
              <h6>Average ETA</h6>
              <h2>{averageETA} min</h2>
            </div>
          </div>
        </div>
      </div>

      <div className="card mb-4">
        <div className="card-header">
          <strong>Live Alerts</strong>
        </div>

        <div className="card-body">
          {alerts.length === 0 ? (
            <p className="text-success mb-0">No active alerts</p>
          ) : (
            alerts.map((alert, index) => (
              <div key={index} className={`alert alert-${alert.type} py-2 mb-2`}>
                {alert.message}
              </div>
            ))
          )}
        </div>
      </div>

      <input
        type="text"
        className="form-control mb-3"
        placeholder="Search vehicle..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      <table className="table table-striped">
        <thead>
          <tr>
            <th>Vehicle</th>
            <th>Driver</th>
            <th>Delivery</th>
            <th>Speed</th>
            <th>Fuel</th>
            <th>Remaining (km)</th>
            <th>ETA (min)</th>
            <th>Latitude</th>
            <th>Longitude</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>
          {filteredVehicles.map((v, index) => (
            <tr key={index}>
              <td>{v.vehicle_id}</td>
              <td>{v.driver_id}</td>
              <td>{v.delivery_id}</td>
              <td>{v.speed}</td>
              <td>{Number(v.fuel_level).toFixed(1)}%</td>
              <td>{Number(v.remaining_distance_km).toFixed(1)}</td>
              <td>{Math.round(v.eta_minutes)} min</td>
              <td>{v.latitude.toFixed(5)}</td>
              <td>{v.longitude.toFixed(5)}</td>
              <td>
                <span
                  className={`badge ${
                    v.status === 'MOVING'
                      ? 'bg-success'
                      : v.status === 'IDLE'
                      ? 'bg-warning text-dark'
                      : 'bg-danger'
                  }`}
                >
                  {v.status}
                </span>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default Dashboard
