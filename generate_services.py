# Service Page Generator
import os

# Service data
services_data = [
    {
        'file': 'environmental-services.html',
        'title': 'Environmental Services',
        'tagline': 'Eco-friendly cleaning and environmental compliance solutions',
        'description': 'Our Environmental Services provide eco-friendly cleaning and maintenance services designed to protect the environment while keeping your spaces pristine. We use sustainable practices and green products to deliver exceptional results.',
        'detail': 'We specialize in implementing environmentally responsible practices that meet compliance requirements while delivering outstanding service quality.',
        'icon': '🌿',
        'img': 'company2.jpg',
        'features': [
            ('🌱', 'Green Cleaning Solutions', 'Eco-friendly cleaning products and methods'),
            ('♻️', 'Waste Management', 'Comprehensive waste handling and recycling'),
            ('📋', 'Environmental Compliance', 'Meeting all regulatory requirements'),
            ('🌍', 'Sustainability Programs', 'Long-term environmental initiatives'),
            ('🧪', 'Safe Chemical Handling', 'Proper handling of all cleaning agents'),
            ('📊', 'Impact Reporting', 'regular environmental impact assessments')
        ]
    },
    {
        'file': 'security-services.html',
        'title': 'Security Services',
        'tagline': 'Comprehensive security solutions to protect your assets',
        'description': 'Our Security Services provide comprehensive protection including personnel, surveillance, and access control systems. We ensure the safety of your facilities, assets, and people with professional security solutions.',
        'detail': 'With trained security professionals and state-of-the-art technology, we deliver reliable protection around the clock.',
        'icon': '🛡️',
        'img': 'company4.jpg',
        'features': [
            ('👮', 'Security Personnel', 'Trained and certified security guards'),
            ('🎥', 'Surveillance Systems', 'Advanced monitoring and CCTV'),
            ('🚪', 'Access Control', 'Electronic access management systems'),
            ('🚨', 'Emergency Response', '24/7 rapid response teams'),
            ('🔒', 'Perimeter Security', 'Comprehensive facility protection'),
            ('📱', 'Mobile Patrols', 'Regular patrol services')
        ]
    },
    {
        'file': 'pest-control.html',
        'title': 'Pest Control',
        'tagline': 'Expert pest management for healthy environments',
        'description': 'Our Pest Control services use safe and effective methods to eliminate and prevent pest infestations. We maintain healthy environments through professional pest management solutions.',
        'detail': 'Using integrated pest management techniques, we provide long-term solutions that are safe for your facility and the environment.',
        'icon': '🐛',
        'img': 'company5.jpg',
        'features': [
            ('🔍', 'Inspection & Assessment', 'Thorough property inspections'),
            ('💊', 'Treatment & Elimination', 'Effective pest removal methods'),
            ('🛡️', 'Preventive Measures', 'Long-term prevention strategies'),
            ('📅', 'Follow-up Services', 'Regular monitoring and maintenance'),
            ('🌿', 'Eco-Friendly Options', 'Green pest control solutions'),
            ('📋', 'Documentation', 'Detailed service reports')
        ]
    },
    {
        'file': 'landscaping.html',
        'title': 'Landscaping Services',
        'tagline': 'Professional landscape design and maintenance',
        'description': 'Our Landscaping Services provide professional landscape design, installation, and maintenance to enhance your property\'s appearance and value.',
        'detail': 'From initial design to ongoing maintenance, we create and maintain beautiful outdoor spaces that make lasting impressions.',
        'icon': '🌳',
        'img': 'company6.jpg',
        'features': [
            ('🎨', 'Landscape Design', 'Custom landscape planning'),
            ('🌱', 'Lawn Maintenance', 'Regular mowing and care'),
            ('💧', 'Irrigation Systems', 'Efficient watering solutions'),
            ('🌺', 'Seasonal Plantings', 'Colorful seasonal displays'),
            ('✂️', 'Tree & Shrub Care', 'Pruning and maintenance'),
            ('🍂', 'Cleanup Services', 'Seasonal cleanup and debris removal')
        ]
    },
    {
        'file': 'electrical-services.html',
        'title': 'Electrical Services',
        'tagline': 'Licensed electrical installation and repair services',
        'description': 'Our Electrical Services provide licensed electricians for installation, maintenance, and emergency electrical services for commercial facilities.',
        'detail': 'We handle all your electrical needs with certified professionals ensuring safety and compliance with all electrical codes.',
        'icon': '⚡',
        'img': 'company7.jpg',
        'features': [
            ('🔧', 'Electrical Repairs', 'Expert troubleshooting and fixes'),
            ('💡', 'Installation Services', 'New equipment installation'),
            ('⚡', 'System Upgrades', 'Electrical system modernization'),
            ('🚨', 'Emergency Services', '24/7 emergency response'),
            ('📊', 'Load Balancing', 'Electrical load optimization'),
            ('🔒', 'Safety Inspections', 'Comprehensive electrical audits')
        ]
    },
    {
        'file': 'plumbing-services.html',
        'title': 'Plumbing Services',
        'tagline': 'Expert plumbing solutions for your facility',
        'description': 'Our Plumbing Services offer expert solutions for repairs, installations, and preventive maintenance to keep your plumbing systems running smoothly.',
        'detail': 'Professional plumbers equipped to handle everything from routine maintenance to complex system installations.',
        'icon': '🔧',
        'img': 'company8.jpg',
        'features': [
            ('🔧', 'Pipe Repairs', 'Expert pipe repair and replacement'),
            ('🚰', 'Fixture Installation', 'Faucets, sinks, and toilets'),
            ('🌊', 'Drain Cleaning', 'Professional drain clearing'),
            ('🔥', 'Water Heater Services', 'Installation and repair'),
            ('💧', 'Leak Detection', 'Advanced leak finding technology'),
            ('🚨', 'emergency Plumbing', '24/7 emergency response')
        ]
    },
    {
        'file': 'hvac-services.html',
        'title': 'HVAC Services',
        'tagline': 'Heating, ventilation, and air conditioning excellence',
        'description': 'Our HVAC Services ensure optimal indoor climate control with professional heating, ventilation, and air conditioning installation, maintenance, and repair.',
        'detail': 'Keep your facility comfortable year-round with our comprehensive HVAC services delivered by certified technicians.',
        'icon': '❄️',
        'img': 'company9.jpg',
        'features': [
            ('❄️', 'AC Installation', 'Professional AC system installation'),
            ('🔥', 'Heating Services', 'Furnace and heating maintenance'),
            ('🔧', 'Maintenance Programs', 'Regular preventive maintenance'),
            ('📊', 'System Optimization', 'Energy efficiency improvements'),
            ('🔄', 'Duct Cleaning', 'Air duct cleaning services'),
            ('🚨', 'Emergency Repairs', '24/7 HVAC emergency service')
        ]
    },
    {
        'file': 'painting-services.html',
        'title': 'Painting Services',
        'tagline': 'Professional interior and exterior painting',
        'description': 'Our Painting Services provide professional interior and exterior painting for commercial and residential properties with attention to detail and quality finishes.',
        'detail': 'Transform your spaces with our expert painting services using premium materials and skilled craftsmanship.',
        'icon': '🎨',
        'img': 'company10.jpg',
        'features': [
            ('🏠', 'Interior Painting', 'Professional indoor painting'),
            ('🏢', 'Exterior Painting', 'Weather-resistant exterior coatings'),
            ('🛠️', 'Surface Preparation', 'Thorough prep for perfect results'),
            ('🎨', 'Color Consultation', 'Expert color selection advice'),
            ('✨', 'Specialty Finishes', 'Decorative and textured finishes'),
            ('🧹', 'Clean-up Services', 'Complete post-project cleanup')
        ]
    },
    {
        'file': 'carpentry.html',
        'title': 'Carpentry Services',
        'tagline': 'Skilled carpentry and custom woodwork',
        'description': 'Our Carpentry Services offer skilled carpentry work including repairs, installations, and custom woodwork solutions for your facility needs.',
        'detail': 'Expert carpenters delivering quality woodwork from simple repairs to complex custom projects.',
        'icon': '🚪',
        'img': 'company11.jpg',
        'features': [
            ('🔨', 'Repairs & Installations', 'All types of carpentry repairs'),
            ('🪵', 'Custom Woodwork', 'Tailored wood solutions'),
            ('🚪', 'Doors & Windows', 'Installation and repair services'),
            ('🗄️', 'Cabinet Work', 'Custom and repair cabinet services'),
            ('📐', 'Trim & Molding', 'Decorative woodwork'),
            ('🛠️', 'Structural Repairs', 'Load-bearing repairs')
        ]
    },
    {
        'file': 'general-maintenance.html',
        'title': 'General Maintenance',
        'tagline': 'Comprehensive facility maintenance services',
        'description': 'Our General Maintenance services provide comprehensive maintenance to keep your facilities in top condition year-round with routine and preventive care.',
        'detail': 'One-stop solution for all your facility maintenance needs, delivered by skilled technicians.',
        'icon': '🔨',
        'img': 'company12.jpg',
        'features': [
            ('📋', 'Routine Inspections', 'Regular facility assessments'),
            ('🔧', 'Preventive Maintenance', 'Scheduled maintenance programs'),
            ('🚨', 'Emergency Repairs', 'Fast response to urgent issues'),
            ('⚙️', 'Equipment Servicing', 'Maintenance of all equipment'),
            ('🏢', 'Building Upkeep', 'Overall facility care'),
            ('📊', 'Maintenance Reports', 'Detailed service documentation')
        ]
    }
]

print('Service data loaded. Ready to generate pages.')
print(f'Total services to generate: {len(services_data)}')
