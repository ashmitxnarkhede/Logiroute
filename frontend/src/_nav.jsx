import React from 'react'
import CIcon from '@coreui/icons-react'
import { cilSpeedometer, cilMap, cilTruck, cilWarning, cilChart, cilSettings } from '@coreui/icons'

import { CNavItem, CNavTitle } from '@coreui/react'

const _nav = [
  {
    component: CNavTitle,
    name: 'LogiRoute',
  },

  {
    component: CNavItem,
    name: 'Dashboard',
    to: '/dashboard',
    icon: <CIcon icon={cilSpeedometer} customClassName="nav-icon" />,
  },

  {
    component: CNavItem,
    name: 'Live Map',
    to: '/live-map',
    icon: <CIcon icon={cilMap} customClassName="nav-icon" />,
  },

  {
    component: CNavItem,
    name: 'Fleet',
    to: '/fleet',
    icon: <CIcon icon={cilTruck} customClassName="nav-icon" />,
  },

  {
    component: CNavItem,
    name: 'Alerts',
    to: '/alerts',
    icon: <CIcon icon={cilWarning} customClassName="nav-icon" />,
  },

  {
    component: CNavItem,
    name: 'Analytics',
    to: '/analytics',
    icon: <CIcon icon={cilChart} customClassName="nav-icon" />,
  },

  {
    component: CNavItem,
    name: 'Settings',
    to: '/settings',
    icon: <CIcon icon={cilSettings} customClassName="nav-icon" />,
  },
]

export default _nav
