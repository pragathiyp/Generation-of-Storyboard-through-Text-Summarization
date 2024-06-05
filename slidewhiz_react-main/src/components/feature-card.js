import React from 'react'

import PropTypes from 'prop-types'

import './feature-card.css'

const FeatureCard = (props) => {
  return (
    <div className="feature-card-container">
      <img
        alt={props.imageAlt}
        src={props.imageSrc}
        className="feature-card-image"
      />
      <h5 className="feature-card-text Headline5">{props.cardTitle}</h5>
      <span className="feature-card-text1">{props.text}</span>
    </div>
  )
}

FeatureCard.defaultProps = {
  cardTitle: 'Title',
  text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed erat nibh tristique ipsum.',
  imageSrc: '/01.svg',
  imageAlt: 'image',
}

FeatureCard.propTypes = {
  cardTitle: PropTypes.string,
  text: PropTypes.string,
  imageSrc: PropTypes.string,
  imageAlt: PropTypes.string,
}

export default FeatureCard
