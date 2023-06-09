package com.findr.findr.controller;

import com.findr.findr.domain.Review;
import com.findr.findr.service.ReviewService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@CrossOrigin(origins = "http://localhost:3000")
@RestController
@Slf4j
public class ReviewController {

    @Autowired
    ReviewService reviewService;

    @GetMapping("/v1/reviews-from-hashes/{restaurantId}")
    private List<Review> getReviewsByRestaurantId(@PathVariable("restaurantId") String restaurantId) {
        log.info("restaurantId: {}", restaurantId);
        return reviewService.getReviewsForRestaurant(restaurantId);
    }

    @PostMapping("/v1/review-submit")
    private void addReview(@RequestBody Review review) {
        reviewService.addReview(review);
    }

    @GetMapping("/v1/get-all-restaurants")
    private Map<String, List<Review>> getAllRestaurants() {
        return reviewService.getAllRestaurants();
    }
}
