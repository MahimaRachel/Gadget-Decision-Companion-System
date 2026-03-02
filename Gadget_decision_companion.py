import streamlit as st
import sqlite3
import pandas as pd

# ========================================
# DATABASE INITIALIZATION
# ========================================
@st.cache_resource
def init_database():
    conn = sqlite3.connect('decision_companion.db', check_same_thread=False)
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS domains (
                    domain TEXT PRIMARY KEY, params TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS ratings (
                    domain TEXT, option TEXT, param TEXT, rating INTEGER,
                    PRIMARY KEY(domain, option, param))''')
    
    domains_data = [
        ('gadgets_laptops',  '["performance","battery","affordability","build","screen","portability"]'),
        ('gadgets_phones',   '["performance","camera","battery","affordability","screen","storage"]'),
        ('gadgets_tablets',  '["performance","battery","affordability","screen_size","portability"]'),
        ('gadgets_speakers', '["sound_quality","battery","affordability","portability","features","durability"]'),
        ('gadgets_watches',  '["fitness_tracking","battery","affordability","design","smart_features","compatibility"]'),
        ('gadgets_earbuds',  '["sound_quality","noise_cancel","battery","affordability","comfort","features"]'),
        ('gadgets_cameras',  '["image_quality","autofocus","battery","affordability","size_weight","video"]'),
    ]
    
    ratings_data = [
        # LAPTOPS
        ('gadgets_laptops', 'Apple MacBook Pro M4', 'performance', 9),
        ('gadgets_laptops', 'Apple MacBook Pro M4', 'battery', 9),
        ('gadgets_laptops', 'Apple MacBook Pro M4', 'price', 4),
        ('gadgets_laptops', 'Apple MacBook Pro M4', 'build', 10),
        ('gadgets_laptops', 'Apple MacBook Pro M4', 'screen', 10),
        ('gadgets_laptops', 'Apple MacBook Pro M4', 'portability', 7),
        ('gadgets_laptops', 'Dell XPS 16', 'performance', 8),
        ('gadgets_laptops', 'Dell XPS 16', 'battery', 7),
        ('gadgets_laptops', 'Dell XPS 16', 'price', 6),
        ('gadgets_laptops', 'Dell XPS 16', 'build', 9),
        ('gadgets_laptops', 'Dell XPS 16', 'screen', 9),
        ('gadgets_laptops', 'Dell XPS 16', 'portability', 8),
        ('gadgets_laptops', 'Lenovo Legion Pro 7i', 'performance', 9),
        ('gadgets_laptops', 'Lenovo Legion Pro 7i', 'battery', 5),
        ('gadgets_laptops', 'Lenovo Legion Pro 7i', 'price', 7),
        ('gadgets_laptops', 'Lenovo Legion Pro 7i', 'build', 8),
        ('gadgets_laptops', 'Lenovo Legion Pro 7i', 'screen', 8),
        ('gadgets_laptops', 'Lenovo Legion Pro 7i', 'portability', 4),
        ('gadgets_laptops', 'Asus Zenbook 14 OLED', 'performance', 7),
        ('gadgets_laptops', 'Asus Zenbook 14 OLED', 'battery', 9),
        ('gadgets_laptops', 'Asus Zenbook 14 OLED', 'price', 8),
        ('gadgets_laptops', 'Asus Zenbook 14 OLED', 'build', 9),
        ('gadgets_laptops', 'Asus Zenbook 14 OLED', 'screen', 9),
        ('gadgets_laptops', 'Asus Zenbook 14 OLED', 'portability', 9),
            # Additional 2025–2026 laptops
        ('gadgets_laptops', 'Lenovo Yoga Slim 9i Aura Edition', 'performance', 8),
        ('gadgets_laptops', 'Lenovo Yoga Slim 9i Aura Edition', 'battery', 9),
        ('gadgets_laptops', 'Lenovo Yoga Slim 9i Aura Edition', 'price', 5),
        ('gadgets_laptops', 'Lenovo Yoga Slim 9i Aura Edition', 'build', 9),
        ('gadgets_laptops', 'Lenovo Yoga Slim 9i Aura Edition', 'screen', 10),
        ('gadgets_laptops', 'Lenovo Yoga Slim 9i Aura Edition', 'portability', 10),

        ('gadgets_laptops', 'Microsoft Surface Laptop 7 15"', 'performance', 8),
        ('gadgets_laptops', 'Microsoft Surface Laptop 7 15"', 'battery', 10),
        ('gadgets_laptops', 'Microsoft Surface Laptop 7 15"', 'price', 5),
        ('gadgets_laptops', 'Microsoft Surface Laptop 7 15"', 'build', 9),
        ('gadgets_laptops', 'Microsoft Surface Laptop 7 15"', 'screen', 9),
        ('gadgets_laptops', 'Microsoft Surface Laptop 7 15"', 'portability', 9),

        ('gadgets_laptops', 'Framework Laptop 13 (AMD Ryzen AI 300)', 'performance', 8),
        ('gadgets_laptops', 'Framework Laptop 13 (AMD Ryzen AI 300)', 'battery', 7),
        ('gadgets_laptops', 'Framework Laptop 13 (AMD Ryzen AI 300)', 'price', 8),
        ('gadgets_laptops', 'Framework Laptop 13 (AMD Ryzen AI 300)', 'build', 8),
        ('gadgets_laptops', 'Framework Laptop 13 (AMD Ryzen AI 300)', 'screen', 8),
        ('gadgets_laptops', 'Framework Laptop 13 (AMD Ryzen AI 300)', 'portability', 9),

        ('gadgets_laptops', 'Razer Blade 16 (2026)', 'performance', 10),
        ('gadgets_laptops', 'Razer Blade 16 (2026)', 'battery', 5),
        ('gadgets_laptops', 'Razer Blade 16 (2026)', 'price', 3),
        ('gadgets_laptops', 'Razer Blade 16 (2026)', 'build', 9),
        ('gadgets_laptops', 'Razer Blade 16 (2026)', 'screen', 10),
        ('gadgets_laptops', 'Razer Blade 16 (2026)', 'portability', 6),

            # Additional 2025–2026 phones
    ('gadgets_phones', 'Xiaomi 15 Ultra', 'performance', 9),
    ('gadgets_phones', 'Xiaomi 15 Ultra', 'camera', 10),
    ('gadgets_phones', 'Xiaomi 15 Ultra', 'battery', 9),
    ('gadgets_phones', 'Xiaomi 15 Ultra', 'price', 7),
    ('gadgets_phones', 'Xiaomi 15 Ultra', 'screen', 9),
    ('gadgets_phones', 'Xiaomi 15 Ultra', 'storage', 9),

    ('gadgets_phones', 'Oppo Find X8 Ultra', 'performance', 9),
    ('gadgets_phones', 'Oppo Find X8 Ultra', 'camera', 10),
    ('gadgets_phones', 'Oppo Find X8 Ultra', 'battery', 8),
    ('gadgets_phones', 'Oppo Find X8 Ultra', 'price', 6),
    ('gadgets_phones', 'Oppo Find X8 Ultra', 'screen', 9),
    ('gadgets_phones', 'Oppo Find X8 Ultra', 'storage', 9),

    ('gadgets_phones', 'Vivo X200 Pro', 'performance', 8),
    ('gadgets_phones', 'Vivo X200 Pro', 'camera', 10),
    ('gadgets_phones', 'Vivo X200 Pro', 'battery', 9),
    ('gadgets_phones', 'Vivo X200 Pro', 'price', 7),
    ('gadgets_phones', 'Vivo X200 Pro', 'screen', 9),
    ('gadgets_phones', 'Vivo X200 Pro', 'storage', 8),

    ('gadgets_phones', 'Honor Magic 7 Pro', 'performance', 9),
    ('gadgets_phones', 'Honor Magic 7 Pro', 'camera', 9),
    ('gadgets_phones', 'Honor Magic 7 Pro', 'battery', 9),
    ('gadgets_phones', 'Honor Magic 7 Pro', 'price', 7),
    ('gadgets_phones', 'Honor Magic 7 Pro', 'screen', 9),
    ('gadgets_phones', 'Honor Magic 7 Pro', 'storage', 9),

        ('gadgets_tablets', 'Apple iPad Air M3 (2025)', 'performance', 9),
    ('gadgets_tablets', 'Apple iPad Air M3 (2025)', 'battery', 9),
    ('gadgets_tablets', 'Apple iPad Air M3 (2025)', 'price', 6),
    ('gadgets_tablets', 'Apple iPad Air M3 (2025)', 'screen_size', 8),
    ('gadgets_tablets', 'Apple iPad Air M3 (2025)', 'portability', 9),

    ('gadgets_tablets', 'Samsung Galaxy Tab S11 Ultra', 'performance', 9),
    ('gadgets_tablets', 'Samsung Galaxy Tab S11 Ultra', 'battery', 9),
    ('gadgets_tablets', 'Samsung Galaxy Tab S11 Ultra', 'price', 5),
    ('gadgets_tablets', 'Samsung Galaxy Tab S11 Ultra', 'screen_size', 10),
    ('gadgets_tablets', 'Samsung Galaxy Tab S11 Ultra', 'portability', 6),

    ('gadgets_tablets', 'OnePlus Pad 3', 'performance', 8),
    ('gadgets_tablets', 'OnePlus Pad 3', 'battery', 9),
    ('gadgets_tablets', 'OnePlus Pad 3', 'price', 8),
    ('gadgets_tablets', 'OnePlus Pad 3', 'screen_size', 8),
    ('gadgets_tablets', 'OnePlus Pad 3', 'portability', 9),

    ('gadgets_tablets', 'Xiaomi Pad 7 Pro', 'performance', 8),
    ('gadgets_tablets', 'Xiaomi Pad 7 Pro', 'battery', 9),
    ('gadgets_tablets', 'Xiaomi Pad 7 Pro', 'price', 8),
    ('gadgets_tablets', 'Xiaomi Pad 7 Pro', 'screen_size', 9),
    ('gadgets_tablets', 'Xiaomi Pad 7 Pro', 'portability', 8),

        ('gadgets_earbuds', 'Nothing Ear (2025)', 'sound_quality', 8),
    ('gadgets_earbuds', 'Nothing Ear (2025)', 'noise_cancel', 8),
    ('gadgets_earbuds', 'Nothing Ear (2025)', 'battery', 8),
    ('gadgets_earbuds', 'Nothing Ear (2025)', 'price', 9),
    ('gadgets_earbuds', 'Nothing Ear (2025)', 'comfort', 9),
    ('gadgets_earbuds', 'Nothing Ear (2025)', 'features', 8),

    ('gadgets_earbuds', 'Technics EAH-AZ100', 'sound_quality', 10),
    ('gadgets_earbuds', 'Technics EAH-AZ100', 'noise_cancel', 9),
    ('gadgets_earbuds', 'Technics EAH-AZ100', 'battery', 8),
    ('gadgets_earbuds', 'Technics EAH-AZ100', 'price', 5),
    ('gadgets_earbuds', 'Technics EAH-AZ100', 'comfort', 8),
    ('gadgets_earbuds', 'Technics EAH-AZ100', 'features', 9),

    ('gadgets_earbuds', 'Devialet Gemini II', 'sound_quality', 9),
    ('gadgets_earbuds', 'Devialet Gemini II', 'noise_cancel', 9),
    ('gadgets_earbuds', 'Devialet Gemini II', 'battery', 7),
    ('gadgets_earbuds', 'Devialet Gemini II', 'price', 4),
    ('gadgets_earbuds', 'Devialet Gemini II', 'comfort', 8),
    ('gadgets_earbuds', 'Devialet Gemini II', 'features', 9),

    ('gadgets_earbuds', 'Jabra Elite 10 Gen 3', 'sound_quality', 8),
    ('gadgets_earbuds', 'Jabra Elite 10 Gen 3', 'noise_cancel', 9),
    ('gadgets_earbuds', 'Jabra Elite 10 Gen 3', 'battery', 8),
    ('gadgets_earbuds', 'Jabra Elite 10 Gen 3', 'price', 7),
    ('gadgets_earbuds', 'Jabra Elite 10 Gen 3', 'comfort', 9),
    ('gadgets_earbuds', 'Jabra Elite 10 Gen 3', 'features', 8),

        ('gadgets_watches', 'Apple Watch Series 11', 'fitness_tracking', 9),
    ('gadgets_watches', 'Apple Watch Series 11', 'battery', 8),
    ('gadgets_watches', 'Apple Watch Series 11', 'price', 4),
    ('gadgets_watches', 'Apple Watch Series 11', 'design', 9),
    ('gadgets_watches', 'Apple Watch Series 11', 'smart_features', 10),
    ('gadgets_watches', 'Apple Watch Series 11', 'compatibility', 9),

    ('gadgets_watches', 'Google Pixel Watch 4 Pro', 'fitness_tracking', 9),
    ('gadgets_watches', 'Google Pixel Watch 4 Pro', 'battery', 8),
    ('gadgets_watches', 'Google Pixel Watch 4 Pro', 'price', 5),
    ('gadgets_watches', 'Google Pixel Watch 4 Pro', 'design', 9),
    ('gadgets_watches', 'Google Pixel Watch 4 Pro', 'smart_features', 9),
    ('gadgets_watches', 'Google Pixel Watch 4 Pro', 'compatibility', 9),

    ('gadgets_watches', 'OnePlus Watch 3', 'fitness_tracking', 8),
    ('gadgets_watches', 'OnePlus Watch 3', 'battery', 10),
    ('gadgets_watches', 'OnePlus Watch 3', 'price', 8),
    ('gadgets_watches', 'OnePlus Watch 3', 'design', 8),
    ('gadgets_watches', 'OnePlus Watch 3', 'smart_features', 8),
    ('gadgets_watches', 'OnePlus Watch 3', 'compatibility', 8),

    ('gadgets_watches', 'Huawei Watch GT 5 Pro', 'fitness_tracking', 9),
    ('gadgets_watches', 'Huawei Watch GT 5 Pro', 'battery', 10),
    ('gadgets_watches', 'Huawei Watch GT 5 Pro', 'price', 7),
    ('gadgets_watches', 'Huawei Watch GT 5 Pro', 'design', 9),
    ('gadgets_watches', 'Huawei Watch GT 5 Pro', 'smart_features', 8),
    ('gadgets_watches', 'Huawei Watch GT 5 Pro', 'compatibility', 7),
        
        ('gadgets_speakers', 'Sony ULT Field 5', 'sound_quality', 8),
    ('gadgets_speakers', 'Sony ULT Field 5', 'battery', 9),
    ('gadgets_speakers', 'Sony ULT Field 5', 'price', 7),
    ('gadgets_speakers', 'Sony ULT Field 5', 'portability', 9),
    ('gadgets_speakers', 'Sony ULT Field 5', 'features', 8),
    ('gadgets_speakers', 'Sony ULT Field 5', 'durability', 9),

    ('gadgets_speakers', 'Bose SoundLink Max 2', 'sound_quality', 9),
    ('gadgets_speakers', 'Bose SoundLink Max 2', 'battery', 8),
    ('gadgets_speakers', 'Bose SoundLink Max 2', 'price', 6),
    ('gadgets_speakers', 'Bose SoundLink Max 2', 'portability', 8),
    ('gadgets_speakers', 'Bose SoundLink Max 2', 'features', 9),
    ('gadgets_speakers', 'Bose SoundLink Max 2', 'durability', 9),

    ('gadgets_speakers', 'Anker Soundcore Motion X600', 'sound_quality', 8),
    ('gadgets_speakers', 'Anker Soundcore Motion X600', 'battery', 9),
    ('gadgets_speakers', 'Anker Soundcore Motion X600', 'price', 8),
    ('gadgets_speakers', 'Anker Soundcore Motion X600', 'portability', 9),
    ('gadgets_speakers', 'Anker Soundcore Motion X600', 'features', 8),
    ('gadgets_speakers', 'Anker Soundcore Motion X600', 'durability', 8),

    ('gadgets_speakers', 'Tribit StormBox Blast 2', 'sound_quality', 8),
    ('gadgets_speakers', 'Tribit StormBox Blast 2', 'battery', 9),
    ('gadgets_speakers', 'Tribit StormBox Blast 2', 'price', 7),
    ('gadgets_speakers', 'Tribit StormBox Blast 2', 'portability', 7),
    ('gadgets_speakers', 'Tribit StormBox Blast 2', 'features', 8),
    ('gadgets_speakers', 'Tribit StormBox Blast 2', 'durability', 10),
    ]
    
    c.executemany("INSERT OR IGNORE INTO domains VALUES(?,?)", domains_data)
    c.executemany("INSERT OR IGNORE INTO ratings VALUES(?,?,?,?)", ratings_data)
    conn.commit()
    return conn

product_links = {
    # Laptops
    "Apple MacBook Pro M4": "https://www.apple.com/macbook-pro/",
    "Dell XPS 16": "https://www.dell.com/en-us/shop/dell-laptops/xps-16-laptop/spd/xps-16-9640-laptop",
    "Lenovo Legion Pro 7i": "https://www.lenovo.com/us/en/p/laptops/legion-laptops/legion-pro-series/legion-pro-7i-gen-9-(16-inch-intel)/len101g0039",
    "Asus Zenbook 14 OLED": "https://www.asus.com/laptops/for-home/zenbook/asus-zenbook-14-oled-ux3405/",

    # Phones
    "iPhone 16 Pro Max": "https://www.apple.com/iphone-16-pro/",
    "Samsung Galaxy S25 Ultra": "https://www.samsung.com/us/smartphones/galaxy-s25-ultra/",
    "Google Pixel 9 Pro": "https://store.google.com/product/pixel_9_pro?hl=en-US",
    "OnePlus 13": "https://www.oneplus.com/us/oneplus-13",

    # Earbuds
    "AirPods Pro 3": "https://www.apple.com/airpods-pro/",
    "Sony WF-1000XM6": "https://www.sony.com/electronics/truly-wireless/wf-1000xm6",
    "Samsung Galaxy Buds 3 Pro": "https://www.samsung.com/us/mobile-audio/galaxy-buds/galaxy-buds3-pro/",
    "Bose QuietComfort Ultra": "https://www.bose.com/p/earbuds/bose-quietcomfort-ultra-earbuds/QCUE-HEADPHONEIN.html",

    # Cameras
    "Sony A7 IV": "https://www.sony.com/electronics/interchangeable-lens-cameras/ilce-7m4",
    "Canon R6 Mark II": "https://www.usa.canon.com/shop/p/eos-r6-mark-ii",
    "Nikon Z8": "https://www.nikonusa.com/p/z-8/1695/overview",
    "Fujifilm X-T5": "https://www.fujifilm-x.com/global/products/cameras/x-t5/",

    # Speakers
    "Sonos Era 300": "https://www.sonos.com/en-us/shop/era-300",
    "JBL Charge 6": "https://www.jbl.com/bluetooth-speakers/CHARGE6-.html",
    "Bose SoundLink Max": "https://www.bose.com/p/speakers/bose-soundlink-max/SLMAX-SPEAKER.html",
    "Ultimate Ears Hyperboom": "https://www.ultimateears.com/en-us/wireless-speakers/hyperboom.html",

    # Tablets
    "Apple iPad Pro M4 (2024/25)": "https://www.apple.com/ipad-pro/",
    "Samsung Galaxy Tab S10 Ultra": "https://www.samsung.com/us/tablets/galaxy-tab-s/galaxy-tab-s10-ultra/",
    "Google Pixel Tablet (2nd gen)": "https://store.google.com/product/pixel_tablet?hl=en-US",
    "Lenovo Yoga Tab Plus": "https://www.lenovo.com/us/en/p/tablets/android-tablets/lenovo-tab-series/yoga-tab-plus/len103l0013",

    # Watches
    "Apple Watch Ultra 3": "https://www.apple.com/apple-watch-ultra-2/",  # Ultra 3 not yet official → link to current Ultra
    "Samsung Galaxy Watch 8 Ultra": "https://www.samsung.com/us/watches/galaxy-watch-ultra/",
    "Google Pixel Watch 4": "https://store.google.com/product/pixel_watch_3?hl=en-US",
    "Garmin Fenix 8": "https://www.garmin.com/en-US/p/929123",
}


def get_product_link(gadget_name):
    return product_links.get(gadget_name, 
                             f"https://www.amazon.com/s?k={gadget_name.replace(' ', '+')}")

# ========================================
# CALCULATION LOGIC (unchanged)
# ========================================
def calculate_decision(options, weights, ratings_df, domain):
    options = [opt.strip() for opt in options if opt.strip()]
    options = list(dict.fromkeys(options))
    if len(options) < 2:
        return None, "Please select at least 2 different options to compare.", [], []

    total_weight = sum(weights.values())
    if total_weight <= 0:
        return None, "Please set at least one priority weight > 0.", [], []

    normalized_weights = {k: v / total_weight for k, v in weights.items()}

    custom_ratings_dict = st.session_state.get('custom_ratings_dict', {})

    results = []
    detailed_scores = []
    fallback_options = []

    for option in options[:20]:
        short_option = option[:57] + "..." if len(option) > 60 else option

        total_score = 0
        param_contributions = {}
        used_custom = False

        for param in normalized_weights:
            if option in custom_ratings_dict and param in custom_ratings_dict[option]:
                rating = custom_ratings_dict[option][param]
                source = "custom user rating"
                used_custom = True
            else:
                row = ratings_df[(ratings_df['option'] == option) & (ratings_df['param'] == param)]
                if not row.empty:
                    rating = row['rating'].iloc[0]
                    source = "database"
                else:
                    rating = 5.0
                    source = "neutral fallback"
                    if option not in fallback_options:
                        fallback_options.append(option)

            rating = max(1, min(10, rating))
            weighted = rating * normalized_weights[param]
            total_score += weighted

            param_contributions[param] = {
                'raw': round(rating, 1),
                'weighted': round(weighted, 2),
                'source': source
            }

        results.append({
            'option': short_option,
            'original_name': option,
            'total_score': total_score,
            'param_count': len(normalized_weights)
        })

        detailed_scores.append({
            'option': option,
            'total_score': total_score,
            'contributions': param_contributions,
            'used_custom': used_custom
        })

    df = pd.DataFrame(results).sort_values('total_score', ascending=False).reset_index(drop=True)
    df['rank'] = df.index + 1

    return df, None, fallback_options, detailed_scores

# ========================================
# ISSUES & SOLUTIONS 
# ========================================
def get_issues_solutions(domain, gadget):

    issues_db = {
        'gadgets_laptops': {
            'Apple MacBook Pro M4': {
                'issues': ['Battery drain in idle', 'High repair costs', 'Thermal throttling under sustained load'],
                'solutions': ['Disable Spotlight indexing', 'Purchase AppleCare+', 'Use a cooling pad']
            },
            'Dell XPS 16': {
                'issues': ['USB-C port reliability issues', 'Overheating during heavy tasks', 'Fan noise under load'],
                'solutions': ['Use high-quality docking station', 'Elevate rear for better airflow', 'Undervolt CPU/GPU if comfortable']
            },
            'Lenovo Legion Pro 7i': {
                'issues': ['Very loud fans during gaming', 'Short battery life', 'Heavy and bulky'],
                'solutions': ['Use balanced/quiet mode when possible', 'Keep plugged in for long sessions', 'Use external monitor + stand']
            },
            'Asus Zenbook 14 OLED': {
                'issues': ['OLED burn-in risk over long term', 'Limited ports', 'Webcam quality average'],
                'solutions': ['Enable pixel shift & screen saver', 'Use USB-C hub/dock', 'External webcam for video calls']
            },
        },

        'gadgets_phones': {
            'iPhone 16 Pro Max': {
                'issues': ['High price', 'No major battery improvement vs previous', 'Overheating during intensive tasks'],
                'solutions': ['Wait for sales / trade-in offers', 'Optimize settings (disable always-on, limit 120 Hz)', 'Avoid heavy use in direct sunlight']
            },
            'Samsung Galaxy S25 Ultra': {
                'issues': ['Still very large & heavy', 'Camera processing sometimes over-sharpened', 'S Pen not as useful for everyone'],
                'solutions': ['Use with case & grip accessory', 'Adjust camera settings (Natural mode)', 'Turn off S Pen features if unused']
            },
            'Google Pixel 9 Pro': {
                'issues': ['Tensor chip still lags behind Snapdragon in raw performance', 'Modem connectivity occasional drops', 'Limited availability in some regions'],
                'solutions': ['Use for photography & AI features rather than gaming', 'Reset network settings when needed', 'Order early or use import']
            },
            'OnePlus 13': {
                'issues': ['OxygenOS still has some bloat vs stock Android', 'Camera tuning not as natural as Pixel', 'No wireless charging in some markets'],
                'solutions': ['Debloat via ADB or use custom launcher', 'Use Pro mode for photography', 'Check regional variant specs']
            },
        },

        'gadgets_tablets': {
            'Apple iPad Pro M4 (2024/25)': {
                'issues': ['Very expensive accessories (pencil, keyboard)', 'No major software differences vs base iPad Pro'],
                'solutions': ['Buy refurbished accessories', 'Consider base model if not doing heavy pro work']
            },
            'Samsung Galaxy Tab S10 Ultra': {
                'issues': ['Very large – not ideal for one-handed use', 'DeX mode still feels half-baked on some apps'],
                'solutions': ['Use with stand or keyboard case', 'Use as secondary monitor or media device instead of full laptop replacement']
            },
            'Google Pixel Tablet (2nd gen)': {
                'issues': ['Charging speaker dock still not perfect', 'Limited high-end app optimization vs iPad'],
                'solutions': ['Use without dock if charging speed matters', 'Mainly for media consumption & light productivity']
            },
            'Lenovo Yoga Tab Plus': {
                'issues': ['Build feels less premium than competitors', 'Software updates slower than Google/Apple'],
                'solutions': ['Good for budget buyers who want kickstand', 'Use as secondary device or media tablet']
            },
        },

        'gadgets_earbuds': {
            'AirPods Pro 3': {
                'issues': ['Battery degradation after ~2 years', 'Fit issues for very small ears'],
                'solutions': ['Turn off ANC during long calls', 'Try third-party memory foam tips']
            },
            'Sony WF-1000XM6': {
                'issues': ['Occasional L/R sound imbalance', 'Case battery drains faster than expected'],
                'solutions': ['Reset through Sony Headphones app', 'Charge case separately']
            },
            'Samsung Galaxy Buds 3 Pro': {
                'issues': ['Stem design not comfortable for all ears', 'ANC weaker than Sony/Bose in some environments'],
                'solutions': ['Try different ear tips (including foam)', 'Use ambient mode in noisy places']
            },
            'Bose QuietComfort Ultra': {
                'issues': ['Bulky case', 'App can be slow to connect sometimes'],
                'solutions': ['Carry case in pocket/bag', 'Force close & reopen app if connection fails']
            },
        },

        'gadgets_cameras': {
            'Sony A7 IV': {
                'issues': ['Overheating during long 4K video shoots', 'Expensive memory card requirements'],
                'solutions': ['Use external fan grip in hot conditions', 'Get fast CFexpress Type A cards']
            },
            'Canon R6 Mark II': {
                'issues': ['Rolling shutter in video mode', 'Battery life shorter than DSLR predecessors'],
                'solutions': ['Shoot in 6K RAW external if possible', 'Carry 2–3 spare batteries']
            },
            'Nikon Z8': {
                'issues': ['Very expensive', 'Ergonomics take time to get used to (no grip included)'],
                'solutions': ['Buy during sales / bundles', 'Add optional battery grip for better handling']
            },
            'Fujifilm X-T5': {
                'issues': ['Autofocus slower than full-frame competitors', 'Battery life average'],
                'solutions': ['Use for stills & retro style shooting', 'Carry spare batteries or power bank']
            },
        },

        'gadgets_speakers': {
            'Sonos Era 300': {
                'issues': ['Requires Wi-Fi (no Bluetooth-only mode)', 'High price for single speaker'],
                'solutions': ['Use as part of multi-room system', 'Wait for sales or buy used/refurbished']
            },
            'JBL Charge 6': {
                'issues': ['Bass can be overpowering indoors', 'Bluetooth connection drops in crowded areas'],
                'solutions': ['Use EQ app to reduce bass', 'Switch to 5 GHz Wi-Fi if available']
            },
            'Bose SoundLink Max': {
                'issues': ['No app EQ on some platforms', 'Heavy for true portability'],
                'solutions': ['Use Bose Music app when available', 'Good for car / home use rather than hiking']
            },
            'Ultimate Ears Hyperboom': {
                'issues': ['Very large & heavy', 'Battery life shorter at max volume'],
                'solutions': ['Best for parties / outdoor gatherings', 'Keep volume moderate to extend playtime']
            },
        },

        'gadgets_watches': {
            'Apple Watch Ultra 3': {
                'issues': ['Large size not comfortable for smaller wrists', 'Battery life shorter with always-on display'],
                'solutions': ['Try on in store first', 'Turn off always-on display when not needed']
            },
            'Samsung Galaxy Watch 8 Ultra': {
                'issues': ['Bulky design', 'Some features limited without Samsung phone'],
                'solutions': ['Good for larger wrists & fitness focus', 'Use Wear OS companion apps on other Android']
            },
            'Google Pixel Watch 4': {
                'issues': ['Battery life still average', 'Limited third-party app ecosystem vs Wear OS competitors'],
                'solutions': ['Charge daily', 'Use for Google ecosystem integration']
            },
            'Garmin Fenix 8': {
                'issues': ['Complex interface for casual users', 'Expensive compared to smartwatches'],
                'solutions': ['Use Garmin Connect app tutorials', 'Consider Forerunner series for lower price']
            },
        }
    }
    if domain in issues_db and gadget in issues_db[domain]:
        data = issues_db[domain][gadget]
        return data['issues'], data['solutions'], None
    else:
        return [], [], "No specific issues recorded for this model."
  

# ========================================
# MAIN APP
# ========================================
def main():
    st.set_page_config(
        page_title="Digital Gadget Decision Companion",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Session state initialization
    if 'compared_models' not in st.session_state:
        st.session_state.compared_models = []
    if 'custom_gadgets' not in st.session_state:
        st.session_state.custom_gadgets = []
    if 'custom_ratings_dict' not in st.session_state:
        st.session_state.custom_ratings_dict = {}
    if 'multiselect_key_suffix' not in st.session_state:
        st.session_state.multiselect_key_suffix = 0

    # Sidebar
    with st.sidebar:
        st.title("Digital Gadget Decision Companion")
        if st.button("How to use", use_container_width=False, type="secondary"):
            with st.expander("Quick Guide", expanded=True):
                st.markdown("""
                1. Select a gadget category  
                2. Choose the models you want to compare  
                3. Adjust your priorities with the sliders  
                4. Click **Get Recommendation** to see results  
                """)
                st.caption("Only selected models are compared")

    # Main content
    st.title("Digital Gadget Decision Companion")
    st.markdown("Compare gadgets objectively • See clear scores • Understand trade-offs")

    conn = init_database()

    # Category selection
    st.subheader("Which Gadget are you looking for..")
    domains = pd.read_sql("SELECT domain FROM domains", conn)['domain'].tolist()
    domain = st.selectbox(
        "Choose your gadget type",
        options=domains,
        format_func=lambda x: x.replace("gadgets_", "").replace("_", " ").title(),
        index=5
    )

    if 'last_domain' not in st.session_state:
        st.session_state.last_domain = domain

    if st.session_state.last_domain != domain:
        st.session_state.compared_models = []
        st.session_state.custom_gadgets = []
        st.session_state.custom_ratings_dict = {}
        st.session_state.multiselect_key_suffix = 0
        st.session_state.last_domain = domain
        st.rerun()
    domain_row = pd.read_sql("SELECT params FROM domains WHERE domain = ?", conn, params=(domain,)).iloc[0]
    params = eval(domain_row['params'])

    # Model selection
    st.subheader("What models are you considering?")
    col_left, col_right = st.columns([4, 2])

    with col_left:
        db_options = pd.read_sql(
            "SELECT DISTINCT option FROM ratings WHERE domain = ? ORDER BY option",
            conn, params=(domain,)
        )['option'].tolist()

        if not db_options:
            st.warning("No models available in this category yet.")
        else:
            dynamic_key = f"models_{domain}_{st.session_state.multiselect_key_suffix}"
            selected_db = st.multiselect(
                f"Available models ({len(db_options)})",
                options=db_options,
                default=st.session_state.compared_models,
                placeholder="Choose models to compare...",
                key=dynamic_key
            )

            if set(selected_db) != set(st.session_state.compared_models):
                st.session_state.compared_models = list(selected_db)
                st.rerun()

    # Custom model input
    with col_right:
        st.markdown("**Add a model not in the list**")

        if 'custom_in_progress' not in st.session_state:
            st.session_state.custom_in_progress = None
            st.session_state.custom_ratings_temp = {}

        if st.session_state.custom_in_progress is None:
            new_name = st.text_input(
                "Model name",
                placeholder="e.g. Nothing Ear (open) 2026",
                key="custom_name_input"
            ).strip()

            if new_name and st.button("Rate this model", type="secondary"):
                existing = st.session_state.compared_models + st.session_state.get('custom_gadgets', [])
                if new_name in existing:
                    st.warning("This name is already in use.")
                elif not new_name:
                    st.warning("Please enter a model name.")
                else:
                    st.session_state.custom_in_progress = new_name
                    st.session_state.custom_ratings_temp = {p: 5.0 for p in params}
                    st.rerun()
        else:
            custom_name = st.session_state.custom_in_progress
            st.info(f"Rate **{custom_name}** (1–10 scale)")

            num_cols = min(3, max(1, len(params)))
            rating_cols = st.columns(num_cols)
            temp_ratings = st.session_state.custom_ratings_temp.copy()

            for i, param in enumerate(params):
                with rating_cols[i % num_cols]:
                    val = st.slider(
                        param.replace("_", " ").title(),
                        1.0, 10.0,
                        temp_ratings.get(param, 5.0),
                        0.5,
                        key=f"custom_rate_{custom_name}_{param}"
                    )
                    temp_ratings[param] = val

            st.session_state.custom_ratings_temp = temp_ratings

            default_count = sum(1 for v in temp_ratings.values() if v == 5.0)
            is_custom_rated = default_count < len(params)

            col_confirm, col_cancel = st.columns(2)
            with col_confirm:
                if st.button("Add to comparison", type="primary", disabled=not is_custom_rated):
                    st.session_state.custom_gadgets.append(custom_name)
                    st.session_state.custom_ratings_dict[custom_name] = temp_ratings.copy()
                    st.session_state.custom_in_progress = None
                    st.session_state.custom_ratings_temp = {}
                    st.success(f"**{custom_name}** added!")
                    st.rerun()

            with col_cancel:
                if st.button("Cancel", type="secondary"):
                    st.session_state.custom_in_progress = None
                    st.session_state.custom_ratings_temp = {}
                    st.rerun()

    # Build final comparison list
    db_selected = st.session_state.compared_models
    custom_selected = st.session_state.get('custom_gadgets', [])
    options = db_selected + custom_selected
    options = list(dict.fromkeys([o.strip() for o in options if o.strip()]))

    # Currently comparing + remove buttons
    st.markdown("**Currently comparing**" + (f" ({len(options)})" if options else ""))

    if options:
        with st.container(border=True):
            for idx, model in enumerate(options):
                col1, col2 = st.columns([5, 1])

                with col1:
                    is_custom = model in custom_selected
                    st.markdown(f"**{model}** (custom)" if is_custom else model)

                with col2:
                    def make_remove_callback(m=model):
                        def _remove():
                            changed = False
                            if m in st.session_state.compared_models:
                                st.session_state.compared_models.remove(m)
                                changed = True
                            if m in st.session_state.get('custom_gadgets', []):
                                st.session_state.custom_gadgets.remove(m)
                                st.session_state.custom_ratings_dict.pop(m, None)
                                changed = True
                            if changed:
                                st.session_state.multiselect_key_suffix += 1
                                st.rerun()
                        return _remove

                    st.button(
                        "×",
                        key=f"rm_{domain}_{idx}_{model.replace(' ','_').replace('(','').replace(')','')}",
                        on_click=make_remove_callback(),
                        type="tertiary",
                        help="Remove from comparison"
                    )
    else:
        st.info("No models selected yet.")

    if options and st.button("Clear all comparisons", type="secondary"):
        st.session_state.compared_models = []
        st.session_state.custom_gadgets = []
        st.session_state.custom_ratings_dict = {}
        st.session_state.multiselect_key_suffix += 1
        st.rerun()

    # Priority sliders
    st.subheader("What features are you looking for?")
    st.markdown("Adjust the sliders according to your priority.")
    weights = {}
    cols = st.columns(min(4, len(params)))

    for i, param in enumerate(params):
        with cols[i % len(cols)]:
            w = st.slider(
                param.replace("_", " ").title(),
                0.0, 10.0, 3.0, 0.5,
                key=f"weight_{domain}_{param}"
            )
            weights[param] = w

    # Get Recommendation button
    st.markdown("<div style='text-align: center; margin: 2.5rem 0 1.8rem 0;'>", unsafe_allow_html=True)

    if st.button(
        "Get Recommendation",
        type="primary",
        disabled=len(options) < 2,
        help="Select at least two models to compare"
    ):
        if len(options) < 2:
            st.error("Please select at least two different models to compare.")
        elif sum(weights.values()) <= 0:
            st.error("Please set at least one priority higher than 0.")
        else:
            with st.spinner("Calculating scores..."):
                try:
                    ratings_df = pd.read_sql(
                        "SELECT * FROM ratings WHERE domain = ?",
                        conn,
                        params=(domain,)
                    )

                    result_df, error, fallbacks, detailed_scores = calculate_decision(
                        options, weights, ratings_df, domain
                    )

                    if error:
                        st.error(error)
                    else:
                        st.caption(f"Compared {len(result_df)} models successfully.")

                        if fallbacks:
                            st.info(
                                "Neutral (5/10) scores used for these models:\n" +
                                "\n".join(f"• {opt}" for opt in fallbacks)
                            )

                        if result_df.empty:
                            st.warning("No valid scores could be calculated.")
                        else:
                            top_row = result_df.iloc[0]
                            top_name = top_row.get('original_name', top_row['option'])

                            link = get_product_link(top_name)
                           

                            st.markdown(f"""
                                <div style="
                                    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
                                    color: white;
                                    padding: 2.4rem 2rem;
                                    border-radius: 16px;
                                    text-align: center;
                                    margin: 1.8rem 0 2.8rem 0;
                                    box-shadow: 0 12px 40px rgba(0,0,0,0.3);
                                    border: 1px solid rgba(255,255,255,0.15);
                                ">
                                    <div style="
                                        font-size: 1.4rem;
                                        opacity: 0.9;
                                        margin-bottom: 0.8rem;
                                        text-transform: uppercase;
                                        letter-spacing: 1px;
                                    ">
                                        Top Recommendation
                                    </div>
                                    <div style="
                                        font-size: 3.2rem;
                                        font-weight: 700;
                                        line-height: 1.1;
                                        margin: 0.3rem 0;
                                    ">
                                        {top_name}
                                    </div>
                                    <div style="
                                        font-size: 1.9rem;
                                        margin-top: 1.2rem;
                                        font-weight: 500;
                                    ">
                                        Score: <strong>{top_row['total_score']:.1f}</strong> / 10
                                    </div>
                                </div>
                                """, unsafe_allow_html=True)
                                     
                            st.subheader("Full Ranking")
                            display_df = result_df[['option', 'total_score']].copy()
                            display_df.columns = ['Model', 'Score']
                            display_df['Score'] = display_df['Score'].round(2)
                            display_df.insert(0, 'Rank', range(1, len(display_df) + 1))
                            st.dataframe(
                                display_df.style.highlight_max(subset=['Score'], color='#d4edda'),
                                use_container_width=True,
                                hide_index=True
                            )

                            
                            st.subheader("Common Future Issues and Fixes")

                            issues_list, solutions_list, msg = get_issues_solutions(domain, top_name)

                            if issues_list:
                                col1, col2 = st.columns(2)
                                with col1:
                                    st.markdown("**Potential Issues**")
                                    for issue in issues_list:
                                        st.markdown(f"• {issue}")
                                with col2:
                                    st.markdown("**Recommended Fixes**")
                                    for sol in solutions_list:
                                        st.markdown(f"• {sol}")
                            else:
                                st.info(msg)

                
                except Exception as e:
                        st.error(f"Calculation failed: {str(e)}")
                        import traceback
                        st.code(traceback.format_exc(), language="python")

                        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("---")
    st.caption("Transparent scoring • Database-driven ")


if __name__ == "__main__":
    main()