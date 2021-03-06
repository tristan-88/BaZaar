import React from 'react';
import {Link} from 'react-router-dom'
import './Footer.css'

function Footer () {

    return (
			<>
				<div className="footer-container">
					{/* <div className="social-media-container"> */}
					<div className="drew-link">
						<h3 style={{ color: "#2b2d42" }}>Drew Thurman</h3>
						<a
							href="https://www.linkedin.com/in/troyd41/"
							target="_blank"
							style={{
								textDecoration: "none",
								fontSize: "2em",
								color: "#006d77",
							}}
						>
							<i className="fab fa-linkedin" style={{ fontSize: "3em" }}></i>
						</a>
					</div>
					<div className="troy-link">
						<h3 style={{ color: "#2b2d42" }}>Troy Dawson</h3>
						<a
							href="https://www.linkedin.com/in/troyd41/"
							target="_blank"
							style={{
								textDecoration: "none",
								fontSize: "2em",
								color: "#006d77",
							}}
						>
							<i className="fab fa-linkedin" style={{ fontSize: "3em" }}></i>
						</a>
					</div>
					<div className="nat-link">
						<h3 style={{ color: "#2b2d42" }}>Nathaniel Ortega</h3>
						<a
							href="https://www.linkedin.com/in/nathaniel-ortega-256673206/"
							target="_blank"
							style={{
								textDecoration: "none",
								fontSize: "2em",
								color: "#006d77",
							}}
						>
							<i className="fab fa-linkedin" style={{ fontSize: "3em" }}></i>
						</a>
					</div>

					<div className="tristan-git">
						<h3 style={{ color: "#2b2d42" }}>Tristan San-Juan</h3>
						<a
							href="https://www.linkedin.com/in/tristan-san-juan-75337920b/"
							target="_blank"
							style={{
								textDecoration: "none",
								fontSize: "2em",
								color: "#006d77",
							}}
						>
							<i className="fab fa-linkedin" style={{ fontSize: "3em" }}></i>
						</a>
					</div>
				</div>
				{/* </div> */}
			</>
		);
}

export default Footer
