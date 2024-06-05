import React from 'react'

import PropTypes from 'prop-types'

import './stats-card.css'

const StatsCard = (props) => {
  return (
    <div className="stats-card-container">
      <img
        alt={props.imageAlt}
        src={props.imageSrc}
        className="stats-card-image"
      />
      <div className="stats-card-container1">
        <h1 className="Headline4">{props.number}</h1>
        <span className="Body1">{props.description}</span>
      </div>
    </div>
  )
}

StatsCard.defaultProps = {
  number: '10',
  imageSrc: '/05.svg',
  description: 'Description',
  imageAlt: 'image',
}

StatsCard.propTypes = {
  number: PropTypes.string,
  imageSrc: PropTypes.string,
  description: PropTypes.string,
  imageAlt: PropTypes.string,
}

export default StatsCard
