package com.findr.findr.domain;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class Review {
    private String reviewHash;
    private String reviewContent;
    private String ownerInfo;
    private String restaurantId;

}
