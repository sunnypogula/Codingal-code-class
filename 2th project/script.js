// DOM Content Loaded
document.addEventListener('DOMContentLoaded', function() {
  // Load events from API
  loadEvents();
  
  // Smooth scrolling for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      
      const targetId = this.getAttribute('href');
      if(targetId === '#') return;
      
      const targetElement = document.querySelector(targetId);
      if(targetElement) {
        window.scrollTo({
          top: targetElement.offsetTop - 80,
          behavior: 'smooth'
        });
      }
    });
  });
});

// Load events from mock API
function loadEvents() {
  // In a real scenario, this would fetch from an actual API
  const mockEvents = [
    {
      id: 1,
      title: "Tech Innovation Summit",
      date: "2023-11-15",
      time: "9:00 AM - 5:00 PM",
      location: "Bahrain Convention Center",
      description: "Annual summit showcasing the latest in technology innovation.",
      image: "http://static.photos/technology/640x360/1"
    },
    {
      id: 2,
      title: "AI Workshop Series",
      date: "2023-12-05",
      time: "2:00 PM - 6:00 PM",
      location: "TKS Innovation Hub",
      description: "Hands-on workshops exploring artificial intelligence applications.",
      image: "http://static.photos/technology/640x360/2"
    },
    {
      id: 3,
      title: "Future of Work Panel",
      date: "2024-01-20",
      time: "6:00 PM - 8:30 PM",
      location: "Royal University Auditorium",
      description: "Experts discuss how technology is transforming the workplace.",
      image: "http://static.photos/office/640x360/1"
    }
  ];

  const eventsContainer = document.getElementById('events-container');
  
  if(eventsContainer) {
    eventsContainer.innerHTML = '';
    
    mockEvents.forEach(event => {
      const eventCard = document.createElement('div');
      eventCard.className = 'bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition duration-300';
      eventCard.innerHTML = `
        <img src="${event.image}" alt="${event.title}" class="w-full h-48 object-cover">
        <div class="p-6">
          <h3 class="text-xl font-semibold text-gray-800 mb-2">${event.title}</h3>
          <div class="flex items-center text-gray-600 mb-2">
            <i data-feather="calendar" class="w-4 h-4 mr-2"></i>
            <span>${event.date} • ${event.time}</span>
          </div>
          <div class="flex items-center text-gray-600 mb-4">
            <i data-feather="map-pin" class="w-4 h-4 mr-2"></i>
            <span>${event.location}</span>
          </div>
          <p class="text-gray-600 mb-4">${event.description}</p>
          <button class="bg-primary hover:bg-primary-600 text-white px-4 py-2 rounded-lg text-sm font-semibold transition duration-300">
            Register Now
          </button>
        </div>
      `;
      eventsContainer.appendChild(eventCard);
    });
    
    feather.replace();
  }
}

// Form submission handler
document.querySelector('form')?.addEventListener('submit', function(e) {
  e.preventDefault();
  alert('Thank you for your message! We will get back to you soon.');
  this.reset();
});