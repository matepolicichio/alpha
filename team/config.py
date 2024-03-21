TEAM_DEFAULTS = {

    'body':
"""<div class="text-center mt-3">
<h6>Nombre</h6>
<p>Posición</p>
</div>
"""
,

    'css_team': 
"""
.team {
    padding: 30px 0px;
}

.team .legend {
  min-height: 110px;
}

.team .legend p {
  font-size: 0.85rem;
}

/* Custom CSS for styling */
.team #carouselTeam {
    overflow: hidden;
    /* Hide overflow to prevent arrows from being cut off */
}

.team .carousel-indicators {
bottom: 0px;
    height: 30px;
    padding: 10px;
    /* Adjust top margin for positioning */
    text-align: center;
    /* Center the indicators */
}

.team .indicator-space {
    height: 40px;
}

.team .carousel-indicators button {
    width: 10px;
    /* Set indicator circle width */
    height: 10px;
    /* Set indicator circle height */
    border-radius: 50%;
    /* Make indicator circle a circle */
    background-color: whitesmoke;
    /* Set indicator circle color */
    margin: 0 5px;
    /* Adjust margin between indicators */
    border: solid 1px gray;
}

.team .carousel-indicators .active {
    width: 12px;
    /* Set active indicator circle width */
    height: 12px;
    /* Set active indicator circle height */
    background-color: black;
    /* Set active indicator circle color */
}

.team .carousel-control-prev,
.team .carousel-control-next {
    background-color: gray;
    /* Set arrow background color to red */
    width: 50px;
    /* Set arrow width */
    height: 50px;
    /* Set arrow height */
    top: 50%;
    /* Position arrows vertically centered */
    transform: translateY(-50%);
    /* Adjust vertical positioning */
    border-radius: 50%;
}

.team .carousel-control-prev-icon,
.team .carousel-control-next-icon {
    border-radius: 50%;
    /* Create a circular arrow icon */
    background-color: gray;
}

"""
,

    'iframe_code':
"""<iframe width="560" height="315" src="https://www.youtube.com/embed/8VCRUY3_elA?si=B_OBL7XY5nHQCP4D" title="YouTube video player" frameborder="0" allow="accelerometer; 
autoplay; 
clipboard-write; 
encrypted-media; 
gyroscope; 
picture-in-picture; 
web-share" allowfullscreen>
</iframe>"""
,
}