def analyze_sentiment(reviews):
    polarity_scores = [TextBlob(review).sentiment.polarity for review in reviews]
    avg_score = sum(polarity_scores) / len(polarity_scores)
    return avg_score * 50 + 50  # scale from 0-100 (approximate)

def generate_summary(reviews):
    positive = [r for r in reviews if TextBlob(r).sentiment.polarity > 0.1]
    negative = [r for r in reviews if TextBlob(r).sentiment.polarity < -0.1]
    neutral = [r for r in reviews if -0.1 <= TextBlob(r).sentiment.polarity <= 0.1]
    summary = f"Positive: {len(positive)}, Negative: {len(negative)}, Neutral: {len(neutral)}\n"
    if positive:
        summary += "\n👍 Positive: " + positive[0]
    if negative:
        summary += "\n👎 Negative: " + negative[0]
    if neutral:
        summary += "\n😐 Neutral: " + neutral[0]
    return summary
def neighborhood_vibe(neighborhood):
    data = neighborhood_data.get(neighborhood)
    if not data:
        return f"Neighborhood '{neighborhood}' not found."
    score = analyze_sentiment(data["reviews"])
    popularity = data["popularity"]
    noise = data["noise"]
    nearby_school = data["nearby_school"]
    nearby_metro = data["nearby_metro"]
    rating = data["rating"]
    summary = generate_summary(data["reviews"])
    return (
        f"\n📍 Neighborhood: {neighborhood}"
        f"\n⭐ Vibe Score: {score:.1f}/100"
        f"\n🔥 Popularity: {popularity}/100"
        f"\n🔊 Noise Level: {noise}"
        f"\n🏫 Nearby School: {nearby_school}"
        f"\n🚇 Nearby Metro: {nearby_metro}"
        f"\n🏅 Rating to Live: {rating}/5"
        f"\n📝 Summary:\n{summary}"
    )
from textblob import TextBlob
neighborhood_data = {
    "Koramangala": {
        "reviews": [
            "Great place to live with lots of cafes and parks nearby.",
            "Traffic is terrible during peak hours, but overall safe.",
            "Friendly community and good schools in the area.",
            "Some noise pollution due to ongoing construction.",
            "Lots of job opportunities around, very vibrant."
        ],
        "popularity": 92,
                "popularity": 92,
                "noise": "Medium",
                "nearby_school": "Yes",
                "nearby_metro": "Yes",
                "rating": 4.5
            },
            "Whitefield": {
                "reviews": [
                    "IT hub with many offices, but very crowded and noisy.",
                    "Public transport is poor, but plenty of shopping malls.",
                    "Safe neighborhood with good restaurants and nightlife.",
                    "Air quality is not great, often smelly and dusty.",
                    "Nice parks but parking is a big issue."
                ],
                "popularity": 88,
                "noise": "High",
                "nearby_school": "Yes",
            "nearby_metro": "Yes",
                "rating": 3.8
            },
            "Hebbal": {
                "reviews": [
                    "Peaceful locality with beautiful lakes and greenery.",
                    "Good connectivity to airport and highways.",
                    "Few entertainment options but very calm and safe.",
                    "Increasing development causing some traffic.",
                    "Clean environment and friendly neighbors."
                ],
                "popularity": 80,
                "noise": "Low",
                "nearby_school": "No",
                "nearby_metro": "Yes",
                "rating": 4.2
            },
            "Gurgaon": {
                "reviews": [
                    "Modern infrastructure and luxury apartments.",
                    "Excellent connectivity to Delhi and airport.",
                    "High cost of living but great amenities.",
                    "Traffic congestion during office hours.",
                    "Plenty of shopping malls and restaurants."
                ],
                "popularity": 95,
                "noise": "High",
                "nearby_school": "Yes",
                "nearby_metro": "Yes",
                "rating": 4.7
            },
            "Noida": {
                "reviews": [
                    "Affordable housing and good schools.",
                    "Metro connectivity is a big plus.",
                    "Some areas face waterlogging in monsoon.",
                    "Rapid development, lots of new projects.",
                    "Safe for families, but pollution is a concern."
                ],
                "popularity": 89,
                "noise": "Medium",
                "nearby_school": "Yes",
                "nearby_metro": "Yes",
                "rating": 4.0
            },
            "Dwarka": {
                "reviews": [
                    "Well-planned locality with wide roads.",
                    "Peaceful and safe, ideal for families.",
                    "Metro access makes commuting easy.",
                    "Limited nightlife but good parks and markets.",
                    "Clean and green environment."
                ],
                "popularity": 85,
                "noise": "Low",
                "nearby_school": "Yes",
                "nearby_metro": "Yes",
                "rating": 4.3
            },
            "South Delhi": {
                "reviews": [
                    "Premium locality with upscale markets.",
                    "Excellent schools and hospitals.",
                    "High property prices, but very posh.",
                    "Good connectivity, but traffic can be bad.",
                    "Lots of cafes, restaurants, and cultural spots."
                ],
                "popularity": 97,
                "noise": "Medium",
                "nearby_school": "Yes",
                "nearby_metro": "Yes",
                "rating": 4.8
            },
            "Sector 128, Noida": {
                "reviews": [
                    "Premium apartments and gated communities.",
                    "Close to major expressways, good connectivity.",
                    "Quiet and clean, but limited shopping options.",
                    "Good schools nearby, safe for families.",
                    "High property prices, but excellent amenities."
                ],
                "popularity": 90,
                "noise": "Low",
                "nearby_school": "Yes",
                "nearby_metro": "No",
                "rating": 4.4
            },
            "Sector 62, Noida": {
                "reviews": [
                    "IT and business hub, lots of offices.",
                    "Metro connectivity is excellent.",
                    "Can be crowded during office hours.",
                    "Affordable housing, good for young professionals.",
                    "Plenty of eateries and shops."
                ],
                "popularity": 87,
                "noise": "Medium",
                "nearby_school": "Yes",
                "nearby_metro": "Yes",
                "rating": 4.1
            },
            "Sector 142, Noida": {
                "reviews": [
                    "Emerging area with new developments.",
                    "Peaceful, less crowded, lots of greenery.",
                    "Limited public transport options.",
                    "Affordable property rates.",
                    "Good for investment, but amenities still growing."
                ],
                "popularity": 80,
                "noise": "Low",
                "nearby_school": "No",
                "nearby_metro": "Yes",
                "rating": 3.7
            },
            "Sector 18, Noida": {
                "reviews": [
                    "Major commercial and shopping area.",
                    "Excellent metro connectivity.",
                    "Very crowded, noisy, and vibrant.",
                    "Lots of restaurants, malls, and entertainment.",
                    "Not ideal for families, but great for shopping and nightlife."
                ],
                "popularity": 93,
                "noise": "High",
                "nearby_school": "No",
                "nearby_metro": "Yes",
                "rating": 3.9
            }
        }

def main():
    print("🏡 Welcome to the Neighborhood Vibe Analyzer")
    neighborhood = input("🔍 Enter neighborhood name (e.g. Koramangala, Whitefield, Hebbal): ").strip()
    result = neighborhood_vibe(neighborhood)
    print(result)

if __name__ == "__main__":
    main()
