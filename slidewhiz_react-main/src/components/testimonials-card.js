import React from 'react'

import PropTypes from 'prop-types'

import './testimonials-card.css'

const TestimonialsCard = (props) => {
  return (
    <div className="testimonials-card-container">
      <img
        alt={props.imageAlt}
        src={props.imageSrc}
        className="testimonials-card-image"
      />
      <div className="testimonials-card-container1">
        <img
          alt={props.imageAlt1}
          src={props.imageSrc1}
          className="testimonials-card-image1"
        />
        <div className="testimonials-card-container2">
          <span className="testimonials-card-text Lead1">{props.text}</span>
          <span className="Subtitle1">{props.text1}</span>
          <span className="testimonials-card-text2 Lead2">{props.text2}</span>
        </div>
      </div>
    </div>
  )
}

TestimonialsCard.defaultProps = {
  imageAlt1: 'image',
  imageAlt: 'image',
  text2: 'Vice President, GoPro',
  text1: 'Floyd Miles',
  text: 'To quickly start my startup landing page design, I was looking for a landing page UI Kit. Landify is one of the best landing page UI kit I have come across. It’s so flexible, well organised and easily editable.',
  imageSrc:
    'https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Airbnb_Logo_B%C3%A9lo.svg/2560px-Airbnb_Logo_B%C3%A9lo.svg.png',
  imageSrc1: '/quote-mark.svg',
}

TestimonialsCard.propTypes = {
  imageAlt1: PropTypes.string,
  imageAlt: PropTypes.string,
  text2: PropTypes.string,
  text1: PropTypes.string,
  text: PropTypes.string,
  imageSrc: PropTypes.string,
  imageSrc1: PropTypes.string,
}

export default TestimonialsCard
