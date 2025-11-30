// Java (Spring Boot) - Example Contact Controller
package com.example.web.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class ContactController {

    // This method handles the POST request when the contact form is submitted
    @PostMapping("/submit-contact")
    public String handleContactForm(
        @RequestParam String name,
        @RequestParam String email,
        @RequestParam String message) {
        
        // 1. In a real application, you would add logic here:
        //    - Validate input (e.g., check email format)
        //    - Log the message to a database
        //    - Send an email notification to the business
        
        System.out.println("Received contact message:");
        System.out.println("Name: " + name);
        System.out.println("Email: " + email);
        System.out.println("Message: " + message);
        
        // 2. Redirect back to the contact section or a thank-you page
        return "redirect:/#contact?success=true"; 
    }
}