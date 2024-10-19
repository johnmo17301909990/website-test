from flask import Flask, request, jsonify
from flask_cors import CORS
from form_checker import check_inquiry_form
from submit_checker import check_inquiry_submit
from floating_form_checker import check_floating_form
from thank_page_checker import check_thank_you_page
from chat_plugin_checker import check_live_chat
from whatsapp_checker import check_whatsapp
from email_checker import check_email_hyperlink
from speed_checker import check_website_speed
from error_page_checker import check_404_error
from mobile_checker import check_mobile_responsive
from google_map_checker import check_google_maps
from error_checker import check_404_page

app = Flask(__name__)
CORS(app)

@app.route('/api/check', methods=['POST'])
def check_website():
    data = request.json
    url = data.get('url')
    checks = data.get('checks', [])

    results = {}

    for check in checks:
        if check == 'inquiryForm':
            results[check] = check_inquiry_form(url)
        elif check == 'inquirySubmit':
            results[check] = check_inquiry_submit(url)
        elif check == 'floatingForm':
            results[check] = check_floating_form(url)
        elif check == 'thankYouPage':
            results[check] = check_thank_you_page(url)
        elif check == 'liveChat':
            results[check] = check_live_chat(url)
        elif check == 'whatsApp':
            results[check] = check_whatsapp(url)
        elif check == 'emailHyperlink':
            results[check] = check_email_hyperlink(url)
        elif check == 'websiteSpeed':
            results[check] = check_website_speed(url)
        elif check == '404Error':
            results[check] = check_404_page(url)
        elif check == 'mobileResponsive':
            results[check] = check_mobile_responsive(url)
        elif check == 'googleMaps':
            results[check] = check_google_maps(url)

    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)