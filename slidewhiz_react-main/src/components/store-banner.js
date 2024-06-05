import React from 'react'

import PropTypes from 'prop-types'

import './store-banner.css'

const StoreBanner = (props) => {
  return (
    <div className="store-banner-store-banner">
      <img
        alt={props.imageAlt1}
        src={props.imageSrc1}
        className="store-banner-image"
      />
      <img
        alt={props.imageAlt}
        src={props.imageSrc}
        className="store-banner-image1"
      />
    </div>
  )
}

StoreBanner.defaultProps = {
  imageSrc: '/app-store-badge-200h.png',
  imageAlt1: 'image',
  imageSrc1: '/google-play-badge-200h.png',
  imageAlt: 'image',
}

StoreBanner.propTypes = {
  imageSrc: PropTypes.string,
  imageAlt1: PropTypes.string,
  imageSrc1: PropTypes.string,
  imageAlt: PropTypes.string,
}

export default StoreBanner
