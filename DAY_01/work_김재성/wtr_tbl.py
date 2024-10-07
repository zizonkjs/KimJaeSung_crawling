from urllib.request import urlopen
from bs4 import BeautifulSoup


# `html_content`는 HTML 문서 내용을 포함하는 문자열이라고 가정합니다.
html_content = """<!DOCTYPE html><html class="no-js">
    <head>
        <!-- Meta -->
        <meta name="viewport" content="width=device-width" />
        <link rel="schema.DC" href="http://purl.org/dc/elements/1.1/" />
        <title>National Weather Service</title>
        <meta name="DC.title" content="National Weather Service" />
        <meta name="DC.description" content="NOAA National Weather Service" />
        <meta name="DC.creator" content="US Department of Commerce, NOAA, National Weather Service" />
        <meta name="DC.date.created" scheme="ISO8601" content="2024-08-11T01:15:11+00:00" />
        <meta name="DC.language" scheme="DCTERMS.RFC1766" content="EN-US" />
        <meta name="DC.keywords" content="weather" />
        <meta name="DC.publisher" content="NOAA's National Weather Service" />
        <meta name="DC.contributor" content="National Weather Service" />
        <meta name="DC.rights" content="/disclaimer.php" />
        <meta name="rating" content="General" />
        <meta name="robots" content="index,follow" />

        <!-- Icons -->
        <link rel="shortcut icon" href="/build/images/favicon.eab6deff.ico" type="image/x-icon" />

                    <link rel="stylesheet" href="/build/app.b5803bc3.css">
        
                    <script src="/build/runtime.5332280c.js"></script><script src="/build/662.4c16084d.js"></script><script src="/build/app.b0ab6b61.js"></script>
            <script type="text/javascript" src="https://cdn.gov.cfigroup.com/webmon/s/source/webmon/ce989efe8b1040/webmon.js" async></script>
            <script type="text/javascript" id="_fed_an_ua_tag" src="https://dap.digitalgov.gov/Universal-Federated-Analytics-Min.js?agency=DOC&amp;subagency=NOAA"></script>
            <script type="text/javascript">
                // GoogleAnalyticsObject is defined in the federated analytics script, but PUA option not used as forecast UA needs sampleRate
                window[window['GoogleAnalyticsObject']]('create', 'UA-40768555-1', 'weather.gov', {'sampleRate': 6});
                window[window['GoogleAnalyticsObject']]('set', 'anonymizeIp', true);
                window[window['GoogleAnalyticsObject']]('require', 'linkid');
                window[window['GoogleAnalyticsObject']]('send', 'pageview');
            </script>
            </head>
    <body>
        <main class="container">
            <header class="row clearfix" id="page-header">
    <a href="//www.noaa.gov" id="header-noaa" class="pull-left"><img src="/build/images/header/noaa.d87e0251.png" alt="National Oceanic and Atmospheric Administration"/></a>
    <a href="https://www.weather.gov" id="header-nws" class="pull-left"><img src="/build/images/header/nws.4e6585d8.png" alt="National Weather Service"/></a>
    <a href="//www.commerce.gov" id="header-doc" class="pull-right"><img src="/build/images/header/doc.b38ba91a.png" alt="United States Department of Commerce"/></a>
</header>

            <nav class="navbar navbar-default row" role="navigation">
    <div class="container-fluid">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#top-nav">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
        </div>
        <div class="collapse navbar-collapse" id="top-nav">
            <ul class="nav navbar-nav">
                <li><a href="//www.weather.gov">HOME</a></li>
                                    <li class="dropdown">
                        <a href="https://www.weather.gov/forecastmaps" class="dropdown-toggle" data-toggle="dropdown">
                                                            FORECAST
                                                        <span class="caret"></span>
                        </a>
                        <ul class="dropdown-menu" role="menu">
                                                                                        <li>
                                    <a href="https://www.weather.gov">Local</a>
                                </li>
                                                            <li>
                                    <a href="https://digital.weather.gov">Graphical</a>
                                </li>
                                                            <li>
                                    <a href="https://www.aviationweather.gov">Aviation</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/marine">Marine</a>
                                </li>
                                                            <li>
                                    <a href="https://water.noaa.gov">Rivers and Lakes</a>
                                </li>
                                                            <li>
                                    <a href="https://www.nhc.noaa.gov">Hurricanes</a>
                                </li>
                                                            <li>
                                    <a href="https://www.spc.noaa.gov">Severe Weather</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/fire">Fire Weather</a>
                                </li>
                                                            <li>
                                    <a href="https://www.esrl.noaa.gov/gmd/grad/solcalc/sunrise.html">Sun/Moon</a>
                                </li>
                                                            <li>
                                    <a href="https://www.cpc.ncep.noaa.gov">Long Range Forecasts</a>
                                </li>
                                                            <li>
                                    <a href="https://www.cpc.ncep.noaa.gov">Climate Prediction</a>
                                </li>
                                                            <li>
                                    <a href="https://www.swpc.noaa.gov">Space Weather</a>
                                </li>
                                                    </ul>
                    </li>
                                    <li class="dropdown">
                        <a href="https://www.weather.gov/wrh/climate" class="dropdown-toggle" data-toggle="dropdown">
                                                            PAST WEATHER
                                                        <span class="caret"></span>
                        </a>
                        <ul class="dropdown-menu" role="menu">
                                                                                        <li>
                                    <a href="https://www.weather.gov/wrh/climate">Past Weather</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/wrh/climate">Heating/Cooling Days</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/wrh/climate">Monthly Temperatures</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/wrh/climate">Records</a>
                                </li>
                                                            <li>
                                    <a href="https://aa.usno.navy.mil">Astronomical Data</a>
                                </li>
                                                    </ul>
                    </li>
                                    <li class="dropdown">
                        <a href="https://www.weather.gov/safety" class="dropdown-toggle" data-toggle="dropdown">
                                                            SAFETY
                                                        <span class="caret"></span>
                        </a>
                        <ul class="dropdown-menu" role="menu">
                                                                                        <li>
                                    <a href="https://www.weather.gov/safety/tsunami">Tsunamis</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/safety/flood">Floods</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/safety/beachhazards">Beach Hazards</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/safety/wildfire">Wildfire</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/safety/cold">Cold</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/safety/tornado">Tornadoes</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/safety/fog">Fog</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/safety/airquality">Air Quality</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/safety/heat">Heat</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/safety/hurricane">Hurricanes</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/safety/lightning">Lightning</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/safety/safeboating">Safe Boating</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/safety/ripcurrent">Rip Currents</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/safety/thunderstorm">Thunderstorms</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/safety/space">Space Weather</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/safety/heat-uv">Sun (Ultraviolet Radiation)</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/safetycampaign">Safety Campaigns</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/safety/wind">Wind</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/safety/drought">Drought</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/safety/winter">Winter Weather</a>
                                </li>
                                                    </ul>
                    </li>
                                    <li class="dropdown">
                        <a href="https://www.weather.gov/informationcenter" class="dropdown-toggle" data-toggle="dropdown">
                                                            INFORMATION
                                                        <span class="caret"></span>
                        </a>
                        <ul class="dropdown-menu" role="menu">
                                                                                        <li>
                                    <a href="https://www.weather.gov/wrn/wea">Wireless Emergency Alerts</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/owlie/publication_brochures">Brochures</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/wrn">Weather-Ready Nation</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/coop">Cooperative Observers</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/briefing">Daily Briefing</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/hazstat">Damage/Fatality/Injury Statistics</a>
                                </li>
                                                            <li>
                                    <a href="http://mag.ncep.noaa.gov">Forecast Models</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/gis">GIS Data Portal</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/nwr">NOAA Weather Radio</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/publications">Publications</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/skywarn">SKYWARN Storm Spotters</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/stormready">StormReady</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/tsunamiready">TsunamiReady</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/notification">Service Change Notices</a>
                                </li>
                                                    </ul>
                    </li>
                                    <li class="dropdown">
                        <a href="https://www.weather.gov/education" class="dropdown-toggle" data-toggle="dropdown">
                                                            EDUCATION
                                                        <span class="caret"></span>
                        </a>
                        <ul class="dropdown-menu" role="menu">
                                                                                        <li>
                                    <a href="https://www.weather.gov/wrn/force">Be A Force of Nature</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/owlie">NWS Education Home</a>
                                </li>
                                                    </ul>
                    </li>
                                    <li class="dropdown">
                        <a href="https://www.weather.gov/news" class="dropdown-toggle" data-toggle="dropdown">
                                                            NEWS
                                                        <span class="caret"></span>
                        </a>
                        <ul class="dropdown-menu" role="menu">
                                                                                        <li>
                                    <a href="https://www.weather.gov/news">NWS News</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/wrn/calendar">Events</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/owlie/publication_brochures">Pubs/Brochures/Booklets </a>
                                </li>
                                                            <li>
                                    <a href="https://www.noaa.gov/NOAA-Communications">NWS Media Contacts</a>
                                </li>
                                                    </ul>
                    </li>
                                    <li class="dropdown">
                        <a href="https://www.weather.gov/search" class="dropdown-toggle" data-toggle="dropdown">
                                                            SEARCH
                                                        <span class="caret"></span>
                        </a>
                        <ul class="dropdown-menu" role="menu">
                                                            <li>
                                    <div id="site-search">
                                        <form method="get" action="//search.usa.gov/search" style="margin-bottom: 0; margin-top: 0;">
                                            <input type="hidden" name="v:project" value="firstgov" />
                                            <label for="query">Search For</label>
                                            <input type="text" name="query" id="query" size="12" />
                                            <input type="submit" value="Go" />
                                            <p>
                                                <input type="radio" name="affiliate" checked="checked" value="nws.noaa.gov" id="nws" />
                                                <label for="nws" class="search-scope">NWS</label>
                                                <input type="radio" name="affiliate" value="noaa.gov" id="noaa" />
                                                <label for="noaa" class="search-scope">All NOAA</label>
                                            </p>
                                        </form>
                                    </div>
                                </li>
                                                                                </ul>
                    </li>
                                    <li class="dropdown">
                        <a href="https://www.weather.gov/about" class="dropdown-toggle" data-toggle="dropdown">
                                                            ABOUT
                                                        <span class="caret"></span>
                        </a>
                        <ul class="dropdown-menu" role="menu">
                                                                                        <li>
                                    <a href="https://www.weather.gov/about">About NWS</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/organization">Organization</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/media/wrn/NWS-2023-Strategic-Plan.pdf">Strategic Plan</a>
                                </li>
                                                            <li>
                                    <a href="https://www.noaa.gov/national-weather-service/commitment-diversity">Commitment to Diversity</a>
                                </li>
                                                            <li>
                                    <a href="https://sites.google.com/a/noaa.gov/nws-insider/">For NWS Employees</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/insider">International</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/ncep">National Centers</a>
                                </li>
                                                            <li>
                                    <a href="https://www.noaa.gov/nws-careers">Careers</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/contact">Contact Us</a>
                                </li>
                                                            <li>
                                    <a href="https://forecast.weather.gov/glossary.php">Glossary</a>
                                </li>
                                                            <li>
                                    <a href="https://www.weather.gov/socialmedia">Social Media</a>
                                </li>
                                                    </ul>
                    </li>
                            </ul>
        </div>
    </div>
</nav>

            <div class="contentArea">
                    <div class="" id="fcst-search">
    <form name="getForecast" id="getForecast" class="form-inline" role="form" action="https://forecast.weather.gov/zipcity.php" method="get" data-baseurl="http://forecast.weather.gov/MapClick.php">
        <div id="getfcst-body">
            <input name="inputstring" type="text" class="form-control" id="inputstring" placeholder="" />
            <input name="btnSearch" id="btnSearch" class="btn btn-default" type="submit" value="Go" />
            <div id="txtHelp"><a href="javascript:void(window.open('http://weather.gov/ForecastSearchHelp.html','locsearchhelp','status=0,toolbar=0,location=0,menubar=0,directories=0,resizable=1,scrollbars=1,height=500,width=530').focus());">View Location Examples</a></div>
        </div>
        <div id="txtError">
            <div id="errorNoResults" style="display:none;">Sorry, the location you searched for was not found. Please try another search.</div>
            <div id="errorMultipleResults" style="display:none">Multiple locations were found. Please select one of the following:</div>
            <div id="errorChoices" style="display:none"></div>
            <input id="btnCloseError" type="button" value="Close" style="display:none" />
        </div>
        <div id="getfcst-head">
                            <p>Your local forecast office is</p>
                <h3 id="getfcst-headOffice">
                    <a href="https://www.weather.gov/mtr">San Francisco Bay Area/Monterey, CA</a>
                </h3>
                    </div>
    </form>
</div>

        <div id="news-items">

            <div id="topnews">
            <div class="icon"><img src="/bundles/templating/images/top_news/important.png"></div>
            <div class="body">
                <h1 style="font-size: 11pt;">Flash Flood Threats in the Mid-Atlantic and Southwest; Fire Weather Threat in the Northwest</h1>
                <p>
                    Showers and thunderstorms with heavy rain will create areas of flash flooding in southeast Virginia through the Carolinas and southern California into Southwest. Isolated severe thunderstorms are possible over parts of the Intermountain West and into the High Plains. Hot and dry conditions continue to pose a fire weather threat especially within the Great Basin.
                                                                <a href="http://www.wpc.ncep.noaa.gov/discussions/hpcdiscussions.php?disc=pmdspd" target="_blank">Read More &gt;</a>
                                    </p>
            </div>
        </div>
    
    </div>

        <!-- PageFormat-Land -->
<script language=javascript>document.title = '7-Day Forecast 37.77N 122.41W';</script><img src="images/track_land_point.png" style="display:none;" />
<!-- Current Conditions -->
<div id="current-conditions" class="panel panel-default">

    <!-- Current Conditions header row -->
    <div class="panel-heading">
        <div>
            <b>Current conditions at</b>
            <h2 class="panel-title">SAN FRANCISCO DOWNTOWN (SFOC1)</h2>
            <span class="smallTxt"><b>Lat:&nbsp;</b>37.77056&deg;N<b>Lon:&nbsp;</b>122.42694&deg;W<b>Elev:&nbsp;</b>150.0ft.</span>
        </div>
    </div>
    <div class="panel-body" id="current-conditions-body">
        <!-- Graphic and temperatures -->
        <div id="current_conditions-summary" class="pull-left" >
                        <p class="myforecast-current">NA</p>
            <p class="myforecast-current-lrg">63&deg;F</p>
            <p class="myforecast-current-sm">17&deg;C</p>
        </div>
        <div id="current_conditions_detail" class="pull-left">
            <table>
            <tr>
            <td class="text-right"><b>Humidity</b></td>
            <td>67%</td>
            </tr>
            <tr>
            <td class="text-right"><b>Wind Speed</b></td>
            <td>NA NA MPH</td>
            </tr>
            <tr>
            <td class="text-right"><b>Barometer</b></td>
            <td>NA</td>
            </tr>
            <tr>
            <td class="text-right"><b>Dewpoint</b></td>
            <td>52&deg;F (11&deg;C)</td>
            </tr>
            <tr>
            <td class="text-right"><b>Visibility</b></td>
            <td>NA</td>
            </tr>
                        <tr>
            <td class="text-right"><b>Last update</b></td>
            <td>
                10 Aug 05:43 PM PDT            </td>
            </tr>
            </table>
        </div>
        <div id="current_conditions_station">
            <div class="current-conditions-extra">
                            <!-- Right hand section -->
            <p class="moreInfo"><b>More Information:</b></p><p><a id="localWFO" href="https://www.weather.gov/mtr" title="San Francisco Bay Area/Monterey, CA"><span class="hideText">Local</span> Forecast Office</a><a id="moreWx" href="https://www.weather.gov/wrh/LocalWeather?zone=CAZ006">More Local Wx</a><a href="https://www.wrh.noaa.gov/mesowest/getobext.php?wfo=mtr&sid=SFOC1&num=72&raw=0">3 Day History</a><a id="wxGraph" href="MapClick.php?lat=37.7772&lon=-122.4168&unit=0&amp;lg=english&amp;FcstType=graphical">Hourly <span class="hideText">Weather </span>Forecast</a></p>            </div>
        <!-- /current_conditions_station -->
        </div>
        <!-- /current-conditions-body -->
    </div>
<!-- /Current Conditions -->
</div>

<!-- 7-Day Forecast -->
<div id="seven-day-forecast" class="panel panel-default">
    <div class="panel-heading">
    <b>Extended Forecast for</b>
    <h2 class="panel-title">
                San Francisco CA    </h2>
    </div>
    <div class="panel-body" id="seven-day-forecast-body">
            <div id="seven-day-forecast-container"><ul id="seven-day-forecast-list" class="list-unstyled"><li class="forecast-tombstone"><div class="tombstone-container"><p class="period-name">Tonight</p><p><img class="forecast-icon" src="newimages/medium/nsct.png" alt="Tonight: Partly cloudy, with a low around 55. West southwest wind 7 to 13 mph, with gusts as high as 20 mph. " title="Tonight: Partly cloudy, with a low around 55. West southwest wind 7 to 13 mph, with gusts as high as 20 mph. " /></p><p class="temp temp-low">Low: 55 &deg;F</p><p class="short-desc">Partly Cloudy</p></div></li><li class="forecast-tombstone"><div class="tombstone-container"><p class="period-name">Sunday</p><p><img class="forecast-icon" src="newimages/medium/bkn.png" alt="Sunday: Mostly cloudy, then gradually becoming sunny, with a high near 66. West southwest wind 6 to 14 mph, with gusts as high as 21 mph. " title="Sunday: Mostly cloudy, then gradually becoming sunny, with a high near 66. West southwest wind 6 to 14 mph, with gusts as high as 21 mph. " /></p><p class="temp temp-high">High: 66 &deg;F</p><p class="short-desc">Decreasing<br>Clouds</p></div></li><li class="forecast-tombstone"><div class="tombstone-container"><p class="period-name">Sunday Night</p><p><img class="forecast-icon" src="newimages/medium/nbkn.png" alt="Sunday Night: Mostly cloudy, with a low around 55. West southwest wind 7 to 13 mph, with gusts as high as 20 mph. " title="Sunday Night: Mostly cloudy, with a low around 55. West southwest wind 7 to 13 mph, with gusts as high as 20 mph. " /></p><p class="temp temp-low">Low: 55 &deg;F</p><p class="short-desc">Mostly Cloudy</p></div></li><li class="forecast-tombstone"><div class="tombstone-container"><p class="period-name">Monday</p><p><img class="forecast-icon" src="newimages/medium/sct.png" alt="Monday: Mostly sunny, with a high near 67. West southwest wind 7 to 14 mph, with gusts as high as 22 mph. " title="Monday: Mostly sunny, with a high near 67. West southwest wind 7 to 14 mph, with gusts as high as 22 mph. " /></p><p class="temp temp-high">High: 67 &deg;F</p><p class="short-desc">Mostly Sunny</p></div></li><li class="forecast-tombstone"><div class="tombstone-container"><p class="period-name">Monday Night</p><p><img class="forecast-icon" src="newimages/medium/nfew.png" alt="Monday Night: Mostly clear, with a low around 54. West wind 6 to 13 mph, with gusts as high as 21 mph. " title="Monday Night: Mostly clear, with a low around 54. West wind 6 to 13 mph, with gusts as high as 21 mph. " /></p><p class="temp temp-low">Low: 54 &deg;F</p><p class="short-desc">Mostly Clear</p></div></li><li class="forecast-tombstone"><div class="tombstone-container"><p class="period-name">Tuesday</p><p><img class="forecast-icon" src="newimages/medium/few.png" alt="Tuesday: Sunny, with a high near 68." title="Tuesday: Sunny, with a high near 68." /></p><p class="temp temp-high">High: 68 &deg;F</p><p class="short-desc">Sunny</p></div></li><li class="forecast-tombstone"><div class="tombstone-container"><p class="period-name">Tuesday Night</p><p><img class="forecast-icon" src="newimages/medium/nsct.png" alt="Tuesday Night: Partly cloudy, with a low around 56." title="Tuesday Night: Partly cloudy, with a low around 56." /></p><p class="temp temp-low">Low: 56 &deg;F</p><p class="short-desc">Partly Cloudy</p></div></li><li class="forecast-tombstone"><div class="tombstone-container"><p class="period-name">Wednesday</p><p><img class="forecast-icon" src="newimages/medium/few.png" alt="Wednesday: Sunny, with a high near 71." title="Wednesday: Sunny, with a high near 71." /></p><p class="temp temp-high">High: 71 &deg;F</p><p class="short-desc">Sunny</p></div></li><li class="forecast-tombstone"><div class="tombstone-container"><p class="period-name">Wednesday Night</p><p><img class="forecast-icon" src="newimages/medium/nfew.png" alt="Wednesday Night: Mostly clear, with a low around 56." title="Wednesday Night: Mostly clear, with a low around 56." /></p><p class="temp temp-low">Low: 56 &deg;F</p><p class="short-desc">Mostly Clear</p></div></li></ul></div>
<script type="text/javascript">
// equalize forecast heights
$(function () {
    var maxh = 0;
    $(".forecast-tombstone .short-desc").each(function () {
        var h = $(this).height();
        if (h > maxh) { maxh = h; }
    });
    $(".forecast-tombstone .short-desc").height(maxh);
});
</script>    </div>
</div>

<!-- Everything between 7-Day Forecast and Footer goes in this row -->
<div id="floatingDivs" class="row">
    <!-- Everything on the left-hand side -->
    <div class="col-md-7 col-lg-8">
        <!-- Detailed Forecast -->
        <div id="detailed-forecast" class="panel panel-default">
        <div class="panel-heading">
            <h2 class="panel-title">Detailed Forecast</h2>
        </div>
        <div class="panel-body" id="detailed-forecast-body">
            <div class="row row-odd row-forecast"><div class="col-sm-2 forecast-label"><b>Tonight</b></div><div class="col-sm-10 forecast-text">Partly cloudy, with a low around 55. West southwest wind 7 to 13 mph, with gusts as high as 20 mph. </div></div><div class="row row-even row-forecast"><div class="col-sm-2 forecast-label"><b>Sunday</b></div><div class="col-sm-10 forecast-text">Mostly cloudy, then gradually becoming sunny, with a high near 66. West southwest wind 6 to 14 mph, with gusts as high as 21 mph. </div></div><div class="row row-odd row-forecast"><div class="col-sm-2 forecast-label"><b>Sunday Night</b></div><div class="col-sm-10 forecast-text">Mostly cloudy, with a low around 55. West southwest wind 7 to 13 mph, with gusts as high as 20 mph. </div></div><div class="row row-even row-forecast"><div class="col-sm-2 forecast-label"><b>Monday</b></div><div class="col-sm-10 forecast-text">Mostly sunny, with a high near 67. West southwest wind 7 to 14 mph, with gusts as high as 22 mph. </div></div><div class="row row-odd row-forecast"><div class="col-sm-2 forecast-label"><b>Monday Night</b></div><div class="col-sm-10 forecast-text">Mostly clear, with a low around 54. West wind 6 to 13 mph, with gusts as high as 21 mph. </div></div><div class="row row-even row-forecast"><div class="col-sm-2 forecast-label"><b>Tuesday</b></div><div class="col-sm-10 forecast-text">Sunny, with a high near 68.</div></div><div class="row row-odd row-forecast"><div class="col-sm-2 forecast-label"><b>Tuesday Night</b></div><div class="col-sm-10 forecast-text">Partly cloudy, with a low around 56.</div></div><div class="row row-even row-forecast"><div class="col-sm-2 forecast-label"><b>Wednesday</b></div><div class="col-sm-10 forecast-text">Sunny, with a high near 71.</div></div><div class="row row-odd row-forecast"><div class="col-sm-2 forecast-label"><b>Wednesday Night</b></div><div class="col-sm-10 forecast-text">Mostly clear, with a low around 56.</div></div><div class="row row-even row-forecast"><div class="col-sm-2 forecast-label"><b>Thursday</b></div><div class="col-sm-10 forecast-text">Sunny, with a high near 70.</div></div><div class="row row-odd row-forecast"><div class="col-sm-2 forecast-label"><b>Thursday Night</b></div><div class="col-sm-10 forecast-text">Partly cloudy, with a low around 56.</div></div><div class="row row-even row-forecast"><div class="col-sm-2 forecast-label"><b>Friday</b></div><div class="col-sm-10 forecast-text">Mostly sunny, with a high near 69.</div></div><div class="row row-odd row-forecast"><div class="col-sm-2 forecast-label"><b>Friday Night</b></div><div class="col-sm-10 forecast-text">Partly cloudy, with a low around 56.</div></div><div class="row row-even row-forecast"><div class="col-sm-2 forecast-label"><b>Saturday</b></div><div class="col-sm-10 forecast-text">Sunny, with a high near 69.</div></div>        </div>
    </div>
    <!-- /Detailed Forecast -->

        
        <!-- Additional Forecasts and Information -->
        <div id="additional_forecasts" class="panel panel-default">
        <div class="panel-heading">
        <h2 class="panel-title">Additional Forecasts and Information</h2>
        </div>

        <div class="panel-body" id="additional-forecasts-body">
        <p class="myforecast-location"><a href="MapClick.php?zoneid=CAZ006">Zone Area Forecast for San Francisco County, CA</a></p>
                <!-- First nine-ten links -->
        <div id="linkBlockContainer">
            <div class="linkBlock">
                <ul class="list-unstyled">
                    <li><a href="https://forecast.weather.gov/product.php?site=MTR&issuedby=MTR&product=AFD&format=CI&version=1&glossary=1">Forecast Discussion</a></li>
                    <li><a href="MapClick.php?lat=37.7772&lon=-122.4168&unit=0&lg=english&FcstType=text&TextType=2">Printable Forecast</a></li>
                    <li><a href="MapClick.php?lat=37.7772&lon=-122.4168&unit=0&lg=english&FcstType=text&TextType=1">Text Only Forecast</a></li>
                </ul>
            </div>
            <div class="linkBlock">
                <ul class="list-unstyled">
                    <li><a href="MapClick.php?lat=37.7772&lon=-122.4168&unit=0&lg=english&FcstType=graphical">Hourly Weather Forecast</a></li>
                    <li><a href="MapClick.php?lat=37.7772&lon=-122.4168&unit=0&lg=english&FcstType=digital">Tabular Forecast</a></li>
                    <!-- <li><a href="afm/PointClick.php?lat=37.7772&lon=-122.4168">Quick Forecast</a></li> -->
                </ul>
            </div>
            <div class="linkBlock">
                <ul class="list-unstyled">
                    <li><a href="//weather.gov/aq/probe_aq_data.php?latitude=37.7772&longitude=-122.4168">Air Quality Forecasts</a></li>
                    <li><a href="MapClick.php?lat=37.7772&lon=-122.4168&FcstType=text&unit=1&lg=en">International System of Units</a></li>
                                        <li><a href="//www.wrh.noaa.gov/forecast/wxtables/index.php?lat=37.7772&lon=-122.4168">Forecast Weather Table Interface</a></li>
                                    </ul>
            </div>
            <!-- /First nine-ten links -->
                <!-- Additional links -->
                    <div class="linkBlock"><ul class="list-unstyled"><li><a href="http://www.wrh.noaa.gov/mtr/versprod.php?pil=RR8&sid=RSA" target="_self">Hourly River Stages</a></li><li><a href="http://www.wrh.noaa.gov/mtr/versprod.php?pil=RR5&sid=RSA" target="_self">Hourly Rainfall</a></li></ul></div><div class="linkBlock"><ul class="list-unstyled"><li><a href="http://www.wrh.noaa.gov/mtr/wxlinks.php" target="_self">NWS Office Map</a></li><li><a href="http://www.wrh.noaa.gov/mtr/wx_calculator.php" target="_self">Weather Calculator</a></li></ul></div><div class="linkBlock"><ul class="list-unstyled"><li><a href="http://www.nws.noaa.gov/wtf/udaf/area/?site=mtr" target="_self">User Defined Area</a></li></ul></div>
        </div> <!-- /linkBlockContainer -->
        </div><!-- /additional-forecasts-body-->
    </div> <!-- /additional_forecasts -->
    </div> <!-- /Everything on the left-hand side -->

    <!-- right-side-data -->
    <div class="col-md-5 col-lg-4" id="right-side-data">
    <div id="mapAndDescriptionArea">
        <!-- openlayer map -->
            <style>
#custom-search{
display: block;
position: relative;
z-index: 50;
top: 52px;
left: 60px;
}
#esri-geocoder-search{
display: block;
position: relative;
z-index: 50;
top: 52px;
left: 60px;
}
#emap{
margin-top:15px;
cursor:pointer;
height:370px;
width:100%;
border: 1px solid #ccc;
border-radius: 3px;
}
#switch-basemap-container{
}
#basemap-selection-form ul{
list-style: none;
 margin: 0px;
}
#basemap-selection-form li{
float: left;
}
.disclaimer{
margin-top:350px;
margin-left: 5px;
z-index: 100;
position: absolute;
text-transform: none;
}
.esriAttributionLastItem{
text-transform: none;
}
.esriSimpleSlider div{
height:22px;
line-height:20px;
width:20px;
}
#point-forecast-map-label {
text-align:center;
font-weight:bold;
color:black;
}
@media (max-width: 767px) {
#emap{
margin-top:.5em;
height:270px;
}
.disclaimer{
margin-top:250px;
}
}
</style>
<!-- forecast-map -->
<div class='point-forecast-map'>
    <div class='point-forecast-map-header text-center'>
        <div id="toolbar">
        <div id="switch-basemap-container">
            <div id="basemap-selection-form" title="Choose a Basemap">
            <div id="basemap-menu">
                <select name="basemap-selected" id="basemap-selected" autocomplete="off" title="Basemap Dropdown Menu">
                <option value="none">Select Basemap</option>
                <option value="topo" selected>Topographic</option>
                <option value="streets">Streets</option>
                <option value="satellite">Satellite</option>
                <option value="ocean">Ocean</option>
                </select>
            </div>
            </div>
            <div id="point-forecast-map-label">
                    Click Map For Forecast
                </div>
        </div><!-- //#switch-basemap-container -->
        <div style="clear:both;"></div>
        </div><!-- //#toolbar -->
    </div><!-- //.point-forecast-map-header -->

    <div id="emap">
        <noscript><center><br><br><b>Map function requires Javascript and a compatible browser.</b></center></noscript>
        <div class="disclaimer"><a href='http://www.weather.gov/disclaimer#esri'>Disclaimer</a></div>
    </div><!-- //#emap -->

    <div class="point-forecast-map-footer">
        <img src="./images/wtf/maplegend_forecast-area.gif" width="100" height="16" alt="Map Legend">
    </div><!-- //.point-forecast-map-footer -->

</div> <!-- //.point-forecast-map -->
<!-- //forecast-map -->
        <!-- //openlayer map -->

        <!-- About this Forecast -->
        <div id="about_forecast" class="panel panel-default">
            <div class="panel-heading collapse-heading clearfix">
                <button type="button" class="menu-toggle" data-toggle="collapse" data-target="#about-forecast-body">
                    <span class="sr-only">Toggle menu</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <div class="collapse-title">
                    <h2 class="panel-title">ABOUT THIS FORECAST</h2>
                </div>
            </div>
            <div>&nbsp;</div>
            <div class="fullRow">
                <div class="left">Point Forecast:</div>
                <div class="right">San Francisco CA<br>&nbsp;37.77&deg;N 122.41&deg;W (Elev. 131 ft)</div>
                    </div>
            <div class="fullRow">
                <div class="left"><a target="_blank" href="//www.weather.gov/glossary/index.php?word=Last+update">Last Update</a>: </div>
                <div class="right">1:27 pm PDT Aug 10, 2024</div>
            </div>
            <div class="fullRow">
                <div class="left"><a target="_blank" href="//www.weather.gov/glossary/index.php?word=forecast+valid+for">Forecast Valid</a>: </div>
                <div class="right">6pm PDT Aug 10, 2024-6pm PDT Aug 17, 2024</div>
            </div>
            <div class="fullRow">
                <div class="left">&nbsp;</div>
                <div class="right"><a href="//forecast.weather.gov/product.php?site=MTR&issuedby=MTR&product=AFD&format=CI&version=1&glossary=1">Forecast Discussion</a></div>
            </div>
            <div class="fullRow">
                <div class="left">&nbsp;</div>
                <div class="right">
                    <a href="MapClick.php?lat=37.7772&lon=-122.4168&unit=0&lg=english&FcstType=kml"><img src="/images/wtf/kml_badge.png" width="45" height="17" alt="Get as KML" /></a>
                    <a href="MapClick.php?lat=37.7772&lon=-122.4168&unit=0&lg=english&FcstType=dwml"><img src="/images/wtf/xml_badge.png" width="45" height="17" alt="Get as XML" /></a>
                </div>
            </div>
        </div>
        <!-- /About this Forecast -->
    </div>
    
        <!--additionalForecast-->
        <div class="panel panel-default" id="additionalForecast">
            <div class="panel-heading">
                <h2 class="panel-title">Additional Resources</h2>
            </div>
            <div class="panel-body">

                <!-- Radar & Satellite Images -->
                <div id="radar" class="subItem">
                    <h4>Radar &amp; Satellite Image</h4>
                    <a href="https://radar.weather.gov/station/kmux/standard"><img src="https://radar.weather.gov/ridge/standard/KMUX_0.gif" class="radar-thumb" alt="Link to Local Radar Data" title="Link to Local Radar Data"></a>                    <a href="https://www.star.nesdis.noaa.gov/GOES/sector.php?sat=G17&sector=psw"><img src="https://cdn.star.nesdis.noaa.gov/GOES17/ABI/SECTOR/psw/GEOCOLOR/600x600.jpg" class="satellite-thumb" alt="Link to Satellite Data" title="Link to Satellite Data"></a>                </div>
                <!-- /Radar & Satellite Images -->
                <!-- Hourly Weather Forecast -->
                <div id="feature" class="subItem">
                    <h4>Hourly Weather Forecast</h4>
                    <a href="MapClick.php?lat=37.7772&lon=-122.4168&unit=0&lg=english&FcstType=graphical"><img src="newimages/medium/hourlyweather.png" class="img-responsive" /></a>
                </div>
                <!-- /Hourly Weather Forecast -->
                <!-- NDFD -->
                <div id="NDFD" class="subItem">
                    <h4>National Digital Forecast Database</h4>
                    <div class="one-sixth-first"><a href="//graphical.weather.gov/sectors/pacsouthwest.php?element=MaxT"><img src="//graphical.weather.gov/images/thumbnail/latest_MaxMinT_pacsouthwest_thumbnail.png" border="0" alt="National Digital Forecast Database Maximum Temperature Forecast" title="National Digital Forecast Database Maximum Temperature Forecast" width="147" height="150"></a>
                <p><a href="//graphical.weather.gov/sectors/pacsouthwest.php?element=MaxT">High Temperature</a></p></div><div class="one-sixth-first"><a href="//graphical.weather.gov/sectors/pacsouthwest.php?element=Wx"><img src="//graphical.weather.gov/images/thumbnail/latest_Wx_pacsouthwest_thumbnail.png" border="0" alt="National Digital Forecast Database Weather Element Forecast" title="National Digital Forecast Database Weather Element Forecast" width="147" height="150"></a>
                <p><a href="//graphical.weather.gov/sectors/pacsouthwest.php?element=Wx">Chance of Precipitation</a></p></div>                </div>
                <!-- /NDFD -->
            </div>
        </div>
        <!-- /additionalForecast -->

    </div>
    <!-- /col-md-4 -->
    <!-- /right-side-data -->
    <script language='javascript'>$( document ).ready(function() { load_openlayers_map('', '', '', '{"centroid_lat":"37.7772","centroid_lon":"-122.4168","lat1":"37.7595","lon1":"-122.4205","lat2":"37.78099995","lon2":"-122.426","lat3":"37.78549995","lon3":"-122.3985","lat4":"37.764","lon4":"-122.393"}') });</script></div>
<!-- /row  -->


</div>
<!-- /PageFormat-Land -->

            </div>
            <footer>
                    <div id="sitemap" class="sitemap-content row">
    <div class="col-xs-12">
        <div class="sitemap-columns">
                                                                                                                <div class="sitemap-section">
                            <div class="panel-heading">
                                <a class="sitemap-section-heading" href="https://alerts.weather.gov">ACTIVE ALERTS</a>
                                <button type="button" class="menu-toggle pull-right" data-toggle="collapse" data-target="#sitemap-1">
                                    <span class="sr-only">Toggle menu</span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                </button>
                            </div>
                            <div class="sitemap-section-body panel-body collapsable collapse" id="sitemap-1">
                                <ul class="list-unstyled">
                                                                            <li><a href=" https://alerts.weather.gov">Warnings By State</a></li>
                                                                            <li><a href="https://www.wpc.ncep.noaa.gov/qpf/excessive_rainfall_outlook_ero.php">Excessive Rainfall</a></li>
                                                                            <li><a href="https://www.wpc.ncep.noaa.gov/wwd/winter_wx.shtml">Winter Weather Forecasts</a></li>
                                                                            <li><a href="https://water.noaa.gov/">River Flooding </a></li>
                                                                            <li><a href="https://www.weather.gov">Latest Warnings</a></li>
                                                                            <li><a href="https://www.spc.noaa.gov/products/outlook/">Thunderstorm/Tornado Outlook </a></li>
                                                                            <li><a href="https://www.nhc.noaa.gov">Hurricanes </a></li>
                                                                            <li><a href="https://www.spc.noaa.gov/products/fire_wx/">Fire Weather Outlooks </a></li>
                                                                            <li><a href="https://www.cpc.ncep.noaa.gov/products/stratosphere/uv_index/uv_alert.shtml">UV Alerts </a></li>
                                                                            <li><a href="https://www.drought.gov">Drought </a></li>
                                                                            <li><a href="https://www.swpc.noaa.gov/products/alerts-watches-and-warnings">Space Weather </a></li>
                                                                            <li><a href="https://www.weather.gov/nwr">NOAA Weather Radio </a></li>
                                                                            <li><a href="https://alerts.weather.gov">NWS CAP Feeds </a></li>
                                                                    </ul>
                            </div>
                        </div>
                                                                    <div class="sitemap-section">
                            <div class="panel-heading">
                                <a class="sitemap-section-heading" href="https://www.weather.gov/wrh/climate">PAST WEATHER</a>
                                <button type="button" class="menu-toggle pull-right" data-toggle="collapse" data-target="#sitemap-1">
                                    <span class="sr-only">Toggle menu</span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                </button>
                            </div>
                            <div class="sitemap-section-body panel-body collapsable collapse" id="sitemap-1">
                                <ul class="list-unstyled">
                                                                            <li><a href="https://www.cpc.ncep.noaa.gov/products/MD_index.shtml">Climate Monitoring </a></li>
                                                                            <li><a href="https://www.weather.gov/wrh/climate">Past Weather </a></li>
                                                                            <li><a href="https://www.weather.gov/wrh/climate">Monthly Temps </a></li>
                                                                            <li><a href="https://www.weather.gov/wrh/climate">Records </a></li>
                                                                            <li><a href="https://www.esrl.noaa.gov/gmd/grad/solcalc/sunrise.html">Astronomical Data </a></li>
                                                                            <li><a href="https://www.climate.gov/maps-data/dataset/past-weather-zip-code-data-table">Certified Weather Data </a></li>
                                                                    </ul>
                            </div>
                        </div>
                                                                                                                                                    <div class="sitemap-section">
                            <div class="panel-heading">
                                <a class="sitemap-section-heading" href="https://www.weather.gov/current">CURRENT CONDITIONS</a>
                                <button type="button" class="menu-toggle pull-right" data-toggle="collapse" data-target="#sitemap-2">
                                    <span class="sr-only">Toggle menu</span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                </button>
                            </div>
                            <div class="sitemap-section-body panel-body collapsable collapse" id="sitemap-2">
                                <ul class="list-unstyled">
                                                                            <li><a href="https://radar.weather.gov">Radar </a></li>
                                                                            <li><a href="https://www.cpc.ncep.noaa.gov/products/monitoring_and_data/">Climate Monitoring </a></li>
                                                                            <li><a href="https://water.noaa.gov/">River Levels </a></li>
                                                                            <li><a href="https://water.noaa.gov/">Observed Precipitation </a></li>
                                                                            <li><a href="https://www.wpc.ncep.noaa.gov/sfc/sfcobs/sfcobs.shtml">Surface Weather </a></li>
                                                                            <li><a href="https://www.spc.noaa.gov/obswx/maps/">Upper Air </a></li>
                                                                            <li><a href="https://www.ndbc.noaa.gov">Marine and Buoy Reports </a></li>
                                                                            <li><a href="https://www.nohrsc.noaa.gov/interactive/html/map.html">Snow Cover </a></li>
                                                                            <li><a href=" https://www.weather.gov/satellite">Satellite </a></li>
                                                                            <li><a href="https://www.swpc.noaa.gov">Space Weather </a></li>
                                                                            <li><a href="http://www.weather.gov/pr">International Observations</a></li>
                                                                    </ul>
                            </div>
                        </div>
                                                                    <div class="sitemap-section">
                            <div class="panel-heading">
                                <a class="sitemap-section-heading" href="https://weather.gov/forecastmaps">FORECAST</a>
                                <button type="button" class="menu-toggle pull-right" data-toggle="collapse" data-target="#sitemap-2">
                                    <span class="sr-only">Toggle menu</span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                </button>
                            </div>
                            <div class="sitemap-section-body panel-body collapsable collapse" id="sitemap-2">
                                <ul class="list-unstyled">
                                                                            <li><a href="https://www.weather.gov">Local Forecast </a></li>
                                                                            <li><a href="https://www.weather.gov/pr">International Forecasts</a></li>
                                                                            <li><a href="https://www.spc.noaa.gov">Severe Weather </a></li>
                                                                            <li><a href="https://www.wpc.ncep.noaa.gov">Current Outlook Maps </a></li>
                                                                            <li><a href="https://www.cpc.ncep.noaa.gov/products/Drought">Drought </a></li>
                                                                            <li><a href="https://www.weather.gov/fire">Fire Weather </a></li>
                                                                            <li><a href="https://www.wpc.ncep.noaa.gov">Fronts/Precipitation Maps </a></li>
                                                                            <li><a href="https://graphical.weather.gov">Current Graphical Forecast Maps </a></li>
                                                                            <li><a href="https://water.noaa.gov">Rivers </a></li>
                                                                            <li><a href="https://www.weather.gov/marine/">Marine </a></li>
                                                                            <li><a href="https://ocean.weather.gov/marine_areas.php">Offshore and High Seas</a></li>
                                                                            <li><a href="http://www.nhc.noaa.gov">Hurricanes </a></li>
                                                                            <li><a href="https://aviationweather.gov">Aviation Weather </a></li>
                                                                            <li><a href="https://www.cpc.ncep.noaa.gov/products/OUTLOOKS_index.shtml">Climatic Outlook </a></li>
                                                                    </ul>
                            </div>
                        </div>
                                                                                                                                                    <div class="sitemap-section">
                            <div class="panel-heading">
                                <a class="sitemap-section-heading" href="https://www.weather.gov/informationcenter">INFORMATION CENTER</a>
                                <button type="button" class="menu-toggle pull-right" data-toggle="collapse" data-target="#sitemap-3">
                                    <span class="sr-only">Toggle menu</span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                </button>
                            </div>
                            <div class="sitemap-section-body panel-body collapsable collapse" id="sitemap-3">
                                <ul class="list-unstyled">
                                                                            <li><a href="https://www.spaceweather.gov">Space Weather </a></li>
                                                                            <li><a href="https://www.weather.gov/briefing/">Daily Briefing </a></li>
                                                                            <li><a href="https://www.weather.gov/marine/">Marine </a></li>
                                                                            <li><a href="https://www.weather.gov/wrh/climate">Climate </a></li>
                                                                            <li><a href="https://www.weather.gov/fire">Fire Weather </a></li>
                                                                            <li><a href="https://www.aviationweather.gov/">Aviation </a></li>
                                                                            <li><a href="http://mag.ncep.noaa.gov/">Forecast Models </a></li>
                                                                            <li><a href="https://water.noaa.gov/">Water </a></li>
                                                                            <li><a href="https://www.weather.gov/gis/">GIS</a></li>
                                                                            <li><a href="https://www.weather.gov/coop/">Cooperative Observers </a></li>
                                                                            <li><a href="https://www.weather.gov/skywarn/">Storm Spotters </a></li>
                                                                            <li><a href="https://www.tsunami.gov">Tsunami Warning System</a></li>
                                                                            <li><a href="https://water.noaa.gov/">National Water Center</a></li>
                                                                            <li><a href="https://www.weather.gov/pr">International Weather</a></li>
                                                                    </ul>
                            </div>
                        </div>
                                                                                                                                                    <div class="sitemap-section">
                            <div class="panel-heading">
                                <a class="sitemap-section-heading" href="https://weather.gov/safety">WEATHER SAFETY</a>
                                <button type="button" class="menu-toggle pull-right" data-toggle="collapse" data-target="#sitemap-4">
                                    <span class="sr-only">Toggle menu</span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                </button>
                            </div>
                            <div class="sitemap-section-body panel-body collapsable collapse" id="sitemap-4">
                                <ul class="list-unstyled">
                                                                            <li><a href="https://www.weather.gov/nwr/">NOAA Weather Radio</a></li>
                                                                            <li><a href="https://www.weather.gov/stormready">StormReady</a></li>
                                                                            <li><a href="https://www.weather.gov/safety/heat">Heat </a></li>
                                                                            <li><a href="https://www.weather.gov/safety/lightning">Lightning </a></li>
                                                                            <li><a href="https://www.nhc.noaa.gov/prepare/">Hurricanes </a></li>
                                                                            <li><a href="https://www.weather.gov/safety/thunderstorm">Thunderstorms </a></li>
                                                                            <li><a href="https://www.weather.gov/safety/tornado">Tornadoes </a></li>
                                                                            <li><a href="https://www.weather.gov/safety/ripcurrent">Rip Currents </a></li>
                                                                            <li><a href="https://www.weather.gov/safety/flood">Floods </a></li>
                                                                            <li><a href="https://www.weather.gov/safety/tsunami">Tsunamis</a></li>
                                                                            <li><a href="https://www.weather.gov/tsunamiready">TsunamiReady</a></li>
                                                                            <li><a href="https://www.weather.gov/safety/winter">Winter Weather </a></li>
                                                                            <li><a href="https://www.weather.gov/safety/heat-uv">Ultra Violet Radiation </a></li>
                                                                            <li><a href="https://airquality.weather.gov">Air Quality </a></li>
                                                                            <li><a href="https://www.weather.gov/hazstat">Damage/Fatality/Injury Statistics </a></li>
                                                                            <li><a href="http://www.redcross.org">Red Cross </a></li>
                                                                            <li><a href="http://www.fema.gov">Federal Emergency Management Agency (FEMA) </a></li>
                                                                            <li><a href="https://www.weather.gov/owlie/publication_brochures">Brochures </a></li>
                                                                            <li><a href="https://www.weather.gov/safety/safeboating">Safe Boating</a></li>
                                                                    </ul>
                            </div>
                        </div>
                                                                                                                                                    <div class="sitemap-section">
                            <div class="panel-heading">
                                <a class="sitemap-section-heading" href="https://weather.gov/news">NEWS</a>
                                <button type="button" class="menu-toggle pull-right" data-toggle="collapse" data-target="#sitemap-5">
                                    <span class="sr-only">Toggle menu</span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                </button>
                            </div>
                            <div class="sitemap-section-body panel-body collapsable collapse" id="sitemap-5">
                                <ul class="list-unstyled">
                                                                            <li><a href="https://weather.gov/news">Newsroom</a></li>
                                                                            <li><a href="https://www.weather.gov/wrn/calendar">Events</a></li>
                                                                            <li><a href="https://www.weather.gov/owlie/publication_brochures">Pubs/Brochures/Booklets </a></li>
                                                                    </ul>
                            </div>
                        </div>
                                                                    <div class="sitemap-section">
                            <div class="panel-heading">
                                <a class="sitemap-section-heading" href="https://www.weather.gov/owlie">EDUCATION</a>
                                <button type="button" class="menu-toggle pull-right" data-toggle="collapse" data-target="#sitemap-5">
                                    <span class="sr-only">Toggle menu</span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                </button>
                            </div>
                            <div class="sitemap-section-body panel-body collapsable collapse" id="sitemap-5">
                                <ul class="list-unstyled">
                                                                            <li><a href="https://www.weather.gov/education">NWS Education Home</a></li>
                                                                            <li><a href="https://www.weather.gov/wrn/force">Be A Force of Nature</a></li>
                                                                            <li><a href="https://www.noaa.gov/education/resource-collections/weather-atmosphere">NOAA Education Resources </a></li>
                                                                            <li><a href="https://forecast.weather.gov/glossary.php">Glossary </a></li>
                                                                            <li><a href="https://www.noaa.gov/jetstream">JetStream </a></li>
                                                                            <li><a href="https://training.weather.gov">NWS Training Portal </a></li>
                                                                            <li><a href="https://library.noaa.gov">NOAA Library </a></li>
                                                                            <li><a href="https://www.weather.gov/owlie">For Students, Parents and Teachers</a></li>
                                                                            <li><a href="http://www.weather.gov/owlie/publication_brochures">Brochures </a></li>
                                                                    </ul>
                            </div>
                        </div>
                                                                                                                                                    <div class="sitemap-section">
                            <div class="panel-heading">
                                <a class="sitemap-section-heading" href="https://www.weather.gov/about">ABOUT</a>
                                <button type="button" class="menu-toggle pull-right" data-toggle="collapse" data-target="#sitemap-6">
                                    <span class="sr-only">Toggle menu</span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                </button>
                            </div>
                            <div class="sitemap-section-body panel-body collapsable collapse" id="sitemap-6">
                                <ul class="list-unstyled">
                                                                            <li><a href="https://www.weather.gov/organization">Organization </a></li>
                                                                            <li><a href="https://www.noaa.gov/NWStransformation">NWS Transformation</a></li>
                                                                            <li><a href="https://www.weather.gov/media/wrn/NWS-2023-Strategic-Plan.pdf">Strategic Plan </a></li>
                                                                            <li><a href="https://www.weather.gov/insider">For NWS Employees </a></li>
                                                                            <li><a href="https://www.weather.gov/international/">International </a></li>
                                                                            <li><a href="https://www.weather.gov/ncep">National Centers </a></li>
                                                                            <li><a href="https://www.weather.gov/tg/">Products and Services </a></li>
                                                                            <li><a href="https://www.noaa.gov/nws-careers">Careers</a></li>
                                                                            <li><a href="https://forecast.weather.gov/glossary.php">Glossary </a></li>
                                                                            <li><a href="https://www.weather.gov/contact">Contact Us </a></li>
                                                                            <li><a href="https://www.weather.gov/socialmedia">Social Media</a></li>
                                                                    </ul>
                            </div>
                        </div>
                                                        </div>
    </div>
</div>

                <div class="footer-legal">
    <div id="footerLogo" class="col-xs-12 col-sm-2 col-md-2">
        <a href="//www.usa.gov"><img src="/css/images/usa_gov.png" alt="usa.gov" width="110" height="30" /></a>
    </div>
    <div class="col-xs-12 col-sm-4 col-md-4">
        <ul class="list-unstyled footer-legal-content">
            <li><a href="//www.commerce.gov">US Dept of Commerce</a></li>
            <li><a href="//www.noaa.gov">National Oceanic and Atmospheric Administration</a></li>
            <li><a href="https://www.weather.gov">National Weather Service</a></li>
            <li><a href="https://www.weather.gov/mtr">San Francisco Bay Area, CA</a>            <li>21 Grace Hopper Ave, Stop 5<br /></li>
                        <li>Monterey, CA 93943-5505</li>
            <li><br /><a href="mailto:w-mtr.webmaster@noaa.gov">Comments? Questions? Please Contact Us.</a></li>
        </ul>
    </div>
    <div class="col-xs-12 col-sm-3 col-md-3">
        <ul class="list-unstyled">
            <li><a href="https://www.weather.gov/disclaimer">Disclaimer</a></li>
            <li><a href="//www.cio.noaa.gov/services_programs/info_quality.html">Information Quality</a></li>
            <li><a href="https://www.weather.gov/help">Help</a></li>
            <li><a href="//www.weather.gov/glossary">Glossary</a></li>
        </ul>
    </div>
    <div class="col-xs-12 col-sm-3 col-md-3">
        <ul class="list-unstyled">
            <li><a href="https://www.weather.gov/privacy">Privacy Policy</a></li>
            <li><a href="https://www.noaa.gov/foia-freedom-of-information-act">Freedom of Information Act (FOIA)</a></li>
            <li><a href="https://www.weather.gov/about">About Us</a></li>
            <li><a href="https://www.weather.gov/careers">Career Opportunities</a></li>
        </ul>
    </div>
</div>

            </footer>
        </main>
    </body>
</html>"""

# BeautifulSoup을 사용하여 HTML 내용을 파싱합니다.
soup = BeautifulSoup(html_content, 'html.parser')

# 모든 일기예보 항목을 찾습니다.
forecasts = soup.find_all('li', class_='forecast-tombstone')

# 각 일기예보 항목을 순회하며 원하는 정보를 추출합니다.
for forecast in forecasts:
    period_name = forecast.find('p', class_='period-name').text
    short_desc = forecast.find('p', class_='short-desc').text
    temp = forecast.find('p', class_='temp').text
    img_title = forecast.find('img')['title']
    
    # 추출한 정보를 한국어로 출력합니다.
    print(f"기간: {period_name}")
    print(f"설명: {short_desc}")
    print(f"온도: {temp}")
    print(f"세부 사항: {img_title}")
    print("-" * 40)

# select 함수를 이용하여 스크래핑
def scraping_use_select(html):
    soup = BeautifulSoup(html, 'html.parser')
    forecasts = soup.select('li.forecast-tombstone')
    
    for forecast in forecasts:
        period_name = forecast.select_one('p.period-name').text
        short_desc = forecast.select_one('p.short-desc').text
        temp = forecast.select_one('p.temp').text
        img_title = forecast.select_one('img')['title']
        
        print(f"기간: {period_name}")
        print(f"설명: {short_desc}")
        print(f"온도: {temp}")
        print(f"세부 사항: {img_title}")
        print("-" * 40)

# 예제 사용
scraping_use_select(html_content)

