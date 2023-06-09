package com.findr.findr.service;

import com.findr.findr.domain.Review;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import static com.findr.findr.domain.SystemCache.RESTAURANT_ID_TO_REVIEW_MAP;

@Service
@Slf4j
public class ReviewService {
    public List<Review> getReviewsForRestaurant(String restaurantId) {
        log.info("restaurantId: {}", restaurantId);
        if (RESTAURANT_ID_TO_REVIEW_MAP.get(restaurantId) == null) {
            log.info("Restaurant does not exist.");
            return new ArrayList<>();
        }
        log.info("Restaurant exists, returning reviews.");
        return RESTAURANT_ID_TO_REVIEW_MAP.get(restaurantId);
    }

    public void addReview(Review review) {
        RESTAURANT_ID_TO_REVIEW_MAP
                .computeIfAbsent(review.getRestaurantId(), k -> new ArrayList<>())
                .add(review);
    }

    public Map<String, List<Review>> getAllRestaurants() {
        return RESTAURANT_ID_TO_REVIEW_MAP;
    }
}
