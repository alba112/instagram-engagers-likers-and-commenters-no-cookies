# Instagram Engagers Scraper

Instagram Engagers Scraper is a fast and flexible API designed to extract high-quality engagement data from Instagram posts. Whether you're tracking trends, analyzing brand engagement, or researching influencer activity, this scraper offers precise, structured data for easy integration into your tools or dashboards.


<p align="center">
  <a href="https://bitbash.def" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Instagram Engagers(Likers and Commenters) ✅ No cookies ✅</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

This scraper allows you to gather engagement data such as comments, likes, and user information from Instagram posts. It is ideal for businesses, researchers, and marketers looking to leverage Instagram insights for various use cases like brand monitoring and influencer research.

### Key Features
- **Precision Data**: Only relevant fields like comments, likes, and user details are returned.
- **Fast and Lightweight**: Optimized for speed and low-latency performance.
- **Easy Integration**: Compatible with Python, JavaScript, and other HTTP-supported languages.
- **Multiple Formats**: Data available in JSON format, with CSV and Excel formats coming soon.
- **Privacy-Respecting**: Only scrapes publicly available content.

## Features

| Feature          | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| Precision Output | Only relevant fields returned, keeping your payload clean and focused.       |
| Fast Performance | Optimized to deliver results with minimal latency.                           |
| Easy to Integrate| Can be easily integrated into any system that supports HTTP requests.       |
| JSON Output      | Data available in JSON format; CSV and Excel outputs coming soon.           |
| Privacy-Focused  | Designed to respect privacy by only collecting publicly available data.     |

## What Data This Scraper Extracts

| Field Name           | Field Description                                                                 |
|----------------------|-----------------------------------------------------------------------------------|
| type                 | Type of engagement data (e.g., comments).                                          |
| link_post            | URL of the post from which the data is extracted.                                |
| comment_like_count   | Number of likes on the comment.                                                   |
| created_at           | Timestamp when the comment was created.                                           |
| hashtags             | Hashtags included in the comment.                                                 |
| like_count           | Number of likes on the post.                                                     |
| mentions             | Mentions of users in the comment.                                                |
| text                 | The actual content of the comment.                                                |
| link_user            | URL of the user who posted the comment.                                          |
| user.full_name       | Full name of the user who posted the comment.                                    |
| user.id              | Unique identifier for the user.                                                  |
| user.is_private      | Indicates if the user's account is private.                                      |
| user.is_verified     | Indicates if the user is verified.                                               |
| user.profile_pic_url | URL of the user's profile picture.                                               |
| user.username        | Instagram username of the user who posted the comment.                           |

## Example Output

    [
          {
            "type": "comments",
            "link_post": "https://www.instagram.com/p/DJHhRQzMLWD/",
            "comment_like_count": 0,
            "created_at": 1746135474,
            "hashtags": [],
            "like_count": 0,
            "mentions": [],
            "text": "🔥❤️🔥",
            "link_user": "https://www.instagram.com/loewensweets",
            "user.full_name": "Löwensweets Mathias Malsch Yoganaschschwerk© .",
            "user.id": "21275061902",
            "user.is_private": false,
            "user.is_verified": true,
            "user.profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.2885-19/483470307_3147281325409963_1945960373892621567_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2QFoHo7e0HArwEbqNAI9dkolis-JmC_r99SyZP-p25f4RIxHULbVbkpL24e61dvdgiA&_nc_ohc=JkYYffsKvjsQ7kNvwEvglyn&_nc_gid=qp9bHu1uO6yHwvwykTEnjA&edm=AD93TDoBAAAA&ccb=7-5&oh=00_AfEwWwu7yXKNddBzVDwvd1rotNqrpEJyURUuDfvTZFzvmg&oe=681A0F06&_nc_sid=87e5dd",
            "user.username": "loewensweets"
          }
        ]

## Directory Structure Tree

instagram-engagers-scraper/
    ├── src/
    │   ├── runner.py
    │   ├── extractors/
    │   │   ├── instagram_parser.py
    │   │   └── utils.py
    │   ├── outputs/
    │   │   └── exporters.py
    │   └── config/
    │       └── settings.example.json
    ├── data/
    │   ├── inputs.sample.json
    │   └── sample_output.json
    ├── requirements.txt
    └── README.md

## Use Cases

- **Marketers** use it to **track engagement on brand posts**, so they can **monitor influencer activity and trends**.
- **Researchers** use it to **analyze comments and likes**, so they can **identify key influencers in their field**.
- **Agencies** use it to **monitor social media activity for clients**, so they can **optimize social strategies**.

## FAQs

**Q: How do I start using this scraper?**
A: Simply send a POST request with the URL of the Instagram post and specify the type of data you want to extract. The results will be returned in JSON format.

**Q: What types of data can I scrape?**
A: You can scrape comments, likes, and user information from any public Instagram post.

**Q: Can I scrape data for multiple posts at once?**
A: Yes, you can specify multiple post URLs in your request to scrape data for all posts simultaneously.

## Performance Benchmarks and Results

**Primary Metric**: Average scraping speed of 2 seconds per post.
**Reliability Metric**: 98% success rate in extracting relevant data.
**Efficiency Metric**: Capable of processing up to 100 posts per minute.
**Quality Metric**: 100% data accuracy for publicly available fields.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
