# Generate all solution detail pages with proper encoding

function Create-SolutionPage {
  param(
    [string]$Category,
    [string]$File,
    [string]$Title,
    [string]$Content
  )
    
  $template = @"
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>$Title | Ideal Solutions</title>
  <link rel="stylesheet" href="../../styles.css">
</head>
<body>
  <header class="header">
    <div class="header-container">
      <a href="../../index.html" class="logo"><span class="logo-text">WALL STREET INTERNATINOL</span></a>
      <div class="menu-toggle"><span></span><span></span><span></span></div>
      <nav class="nav">
        <a href="../../index.html" class="nav-link">Home</a>
        <a href="../who-we-are.html" class="nav-link">Who We Are</a>
        <a href="../our-team.html" class="nav-link">Our Team</a>
        <a href="../our-solutions.html" class="nav-link active">Solutions</a>
        <a href="../news.html" class="nav-link">News</a>
        <a href="../careers.html" class="nav-link">Careers</a>
        <a href="../contact-us.html" class="nav-link">Contact Us</a>
      </nav>
    </div>
  </header>
  <section class="hero">
    <div class="hero-content">
      <h1>$Title</h1>
    </div>
  </section>
  <div class="breadcrumb">
    <div class="breadcrumb-container">
      <a href="../../index.html">Home</a>
      <span class="breadcrumb-separator">/</span>
      <a href="../our-solutions.html">Solutions</a>
      <span class="breadcrumb-separator">/</span>
      <span class="breadcrumb-current">$Title</span>
    </div>
  </div>
  <section class="section">
    <div class="container">
      <div class="solution-detail">
        <div class="solution-detail-content">
          <p>$Content</p>
        </div>
      </div>
    </div>
  </section>
  <section class="contact-cta">
    <div class="container">
      <h2>Let's talk</h2>
      <p>Ready to explore new horizons? Reach out and connect with us today!</p>
      <a href="../contact-us.html" class="btn btn-primary">Contact Us</a>
    </div>
  </section>
  <footer class="footer">
    <div class="footer-container">
      <div class="footer-grid">
        <div class="footer-section">
          <h3>Quick Links</h3>
          <ul class="footer-links">
            <li><a href="../../index.html">Home</a></li>
            <li><a href="../who-we-are.html">Who We Are</a></li>
            <li><a href="../our-team.html">Our Team</a></li>
            <li><a href="../our-solutions.html">Solutions</a></li>
          </ul>
        </div>
        <div class="footer-section">
          <h3>More Links</h3>
          <ul class="footer-links">
            <li><a href="../news.html">News</a></li>
            <li><a href="../careers.html">Careers</a></li>
            <li><a href="../contact-us.html">Contact Us</a></li>
          </ul>
        </div>
        <div class="footer-section">
          <h3>Connect With Us</h3>
          <div class="social-links">
            <a href="#" class="social-link">in</a>
            <a href="#" class="social-link">ig</a>
            <a href="#" class="social-link">fb</a>
            <a href="#" class="social-link">tw</a>
            <a href="#" class="social-link">yt</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <div class="footer-legal">
          <a href="#">Sitemap</a>
          <a href="#">Terms & Condition</a>
          <a href="#">Privacy Policy</a>
        </div>
        <p>&copy; 2023 Ideal Solutions</p>
      </div>
    </div>
  </footer>
  <script src="../../scripts/main.js"></script>
</body>
</html>
"@
    
  $filePath = "d:\anitha\website\pages\$Category\$File"
  Set-Content -Path $filePath -Value $template -Encoding UTF8
}

# IT Solutions
Create-SolutionPage -Category "it-solutions" -File "homeland-security.html" -Title "Homeland Security and Civil Defense Solutions" -Content "Ideal Solutions - Your Ultimate Homeland Security and Civil Defense Partner, providing rapid, accurate, and reliable solutions that safeguard precious lives and invaluable assets."

Create-SolutionPage -Category "it-solutions" -File "ideal-unity.html" -Title "Ideal Unity" -Content "Introducing Ideal Unity, your ultimate destination for comprehensive business management. With a robust suite of features meticulously designed to nurture every aspect of your enterprise, we redefine efficiency and productivity."

Create-SolutionPage -Category "it-solutions" -File "iot-fleet-management.html" -Title "IoT Fleet Management and Dispatching Solutions" -Content "Discover the future of fleet management with Ideal Solutions IOT Fleet Management and Dispatching Solution. Our customized solution empowers you to take charge of your fleet like never before."

Create-SolutionPage -Category "it-solutions" -File "ibusbuddyhtml" -Title "iBusBuddySolution" -Content "Our innovative iBusBuddy Solution is meticulously crafted to deliver users a flawless and user-centric encounter, ensuring swift and effortless access to real-time bus schedules."

Create-SolutionPage -Category "it-solutions" -File "rugged-devices.html" -Title "Rugged Devices" -Content "Explore Unmatched Rugged Performance with Getac Devices at Ideal Solutions! Welcome to the Future of Rugged Technology where durability meets innovation."

# Payment Solutions
Create-SolutionPage -Category "payment-solutions" -File "contactless-vending.html" -Title "Contactless Payment Vending Machines" -Content "Welcome to the future of vending - Contactless Payment Vending Machines by Ideal Solutions. Elevating convenience and safety our state-of-the-art machines redefine the way transactions are made."

Create-SolutionPage -Category "payment-solutions" -File "all-in-one-payment.html" -Title "All-In-One Smart Electronic Payment Solutions" -Content "Introducing the pinnacle of convenience and security - Ideal All-in-One Smart Electronic Payment Solutions. Our comprehensive suite of payment touch points seamlessly handles all acceptance media and form factors."

Create-SolutionPage -Category "payment-solutions" -File "self-service-kiosk.html" -Title "Self-Service Kiosk" -Content "Unlock a world of seamless interactions and unparalleled convenience with Ideal Self-Service Kiosks. With an extensive array of smart solutions we cater to every need revolutionizing the way you engage with your customers."

Create-SolutionPage -Category "payment-solutions" -File "unattended-terminals.html" -Title "Unattended Payment Terminals" -Content "Introducing the ultimate answer to your integration needs - Ideal Unattended Payment Terminals. Embrace a world of seamless transactions and heightened convenience."

Create-SolutionPage -Category "payment-solutions" -File "smart-pos.html" -Title "Smart Point of Sales (POS)" -Content "Welcome to Ideal Solutions your comprehensive point of sale (POS) system provider delivering a synergistic blend of cutting-edge technologies and unwavering support."

Create-SolutionPage -Category "payment-solutions" -File "secured-network.html" -Title "Secured Payment Network Solutions" -Content "Welcome to the evolution of payments with Ideal Secured Payment Network Solutions. Since 1998 we have been at the forefront of developing and delivering high-end payment solutions."

# GIS Solutions
Create-SolutionPage -Category "gis-solutions" -File "gis-development.html" -Title "GIS Application Development" -Content "Welcome to the realm of geospatial excellence with Ideal Solutions. As a trailblazer in the field of GIS Software Development we bring to you a world where data meets geography."

Create-SolutionPage -Category "gis-solutions" -File "gis-training.html" -Title "GIS Training and Support" -Content "Discover the power of tailored GIS training and support through Ideal GIS Training and Support. Unlock the full potential of your GIS investment with courses meticulously designed."

Create-SolutionPage -Category "gis-solutions" -File "3d-mapping.html" -Title "3D and HD Mapping" -Content "Welcome to a realm where mapping transcends boundaries and insights are redefined. With Ideal 3D and HD Mapping we're crafting the next generation of GIS data that fuels innovation."

Create-SolutionPage -Category "gis-solutions" -File "satellite-imagery.html" -Title "Satellite Imagery Processing" -Content "Welcome to the realm of boundless perspectives - Satellite Imagery Processing by Ideal Solutions. Unveil the power of satellite imagery harnessed and transformed into actionable insights."

Create-SolutionPage -Category "gis-solutions" -File "bim-gis.html" -Title "BIM and GIS Integration" -Content "Welcome to the realm where location intelligence and design prowess converge - Ideal BIM and GIS Integration. We provide more than just a framework we empower analysis and decision-making."

Create-SolutionPage -Category "gis-solutions" -File "gis-consultancy.html" -Title "GIS Consultancy" -Content "Welcome to the realm of expert GIS solutions precisely calibrated to meet your unique parameters. At Ideal GIS Consultancy we're not just consultants we're architects of efficiency."

Create-SolutionPage -Category "gis-solutions" -File "remote-sensing.html" -Title "Remote Sensing" -Content "Embark on a journey of credible data and unparalleled insights with Ideal Remote Sensing. As pioneers in the field we harness the power of remote sensing to gather monitor and assess information."

Create-SolutionPage -Category "gis-solutions" -File "lidar.html" -Title "Light Detection and Ranging (LiDAR)" -Content "Welcome to the forefront of rapid and cost-effective data intelligence visualization and analytics with Ideal LiDAR Solutions. LiDAR data stands as your ticket to a detailed digital twin."

Write-Output "All solution pages created successfully!"
