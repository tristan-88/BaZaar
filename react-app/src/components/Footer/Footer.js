import React from 'react';
import {Link} from 'react-router-dom'
import './Footer.css'

function Footer () {

    return (
        <>
            <div className="footer-container">
            {/* <div className="social-media-container"> */}

                      <div className='linkedin-container'>
                            <div className='troy-link'>
                         <a href="https://www.linkedin.com/in/troyd41/"  style={{textDecoration:'none', fontSize:"2em"}}><i class="fab fa-linkedin" style={{fontSize: '3em'}}></i></a>
                            </div>
                            <div className='drew-link'>
                         <a href="https://www.linkedin.com/in/drew-thurman/"  style={{textDecoration:'none', fontSize:"2em"}}><i class="fab fa-linkedin" style={{fontSize: '3em'}}></i></a>
                            </div>
                            <div className='Nat-link'>
                         <a href="https://www.linkedin.com/in/nathaniel-ortega-256673206/"  style={{textDecoration:'none', fontSize:"2em"}}><i class="fab fa-linkedin" style={{fontSize: '3em'}}></i></a>
                            </div>
                    </div>
                </div>
            {/* </div> */}
        </>
    )
}

export default Footer
