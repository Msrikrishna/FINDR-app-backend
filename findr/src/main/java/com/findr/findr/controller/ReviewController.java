package com.findr.findr.controller;

import com.findr.findr.domain.Review;
import com.findr.findr.service.ReviewService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@Slf4j
public class ReviewController {

    @Autowired
    ReviewService reviewService;

    @GetMapping("/v1/reviews-from-hashes/{restaurantId}")
    private List<Review> getReviewsByRestaurantId(@PathVariable("restaurantId") String restaurantId) {
        return reviewService.getReviewsForRestaurant(restaurantId);
    }

    @PostMapping("/v1/review-submit")
    private void addReview(@RequestBody Review review) {
        reviewService.addReview(review);
    }
}
