const API_URL = 'http://localhost:8000'

export async function getLiveFleet() {
  const response = await fetch(`${API_URL}/fleet/live`)

  if (!response.ok) {
    throw new Error('Failed to fetch fleet data')
  }

  return await response.json()
}
