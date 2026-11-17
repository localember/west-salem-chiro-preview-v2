#!/usr/bin/env python3
"""Build the West Salem Chiropractic homepage mockup (design preview only)."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LEGAL_SRC = ROOT / "legal-pages.json"
OUT = ROOT

PHONE_DISPLAY = "(608) 786-3304"
PHONE_TEL = "+16087863304"
MAPS = "https://goo.gl/maps/qYiYvvvt3Vu5DSAy7"
MAP_EMBED = "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d4834.709969600709!2d-91.09181832154394!3d43.9027394520625!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87feafa62408a155%3A0xdcf5f48b35c5ee34!2sWest%20Salem%20Chiropractic!5e0!3m2!1sen!2sus!4v1650037947468!5m2!1sen!2sus"
FACEBOOK = "https://www.facebook.com/West-Salem-Chiropractic-100434905993717"
ADDRESS_LINES = "640 Commerce St Suite A<br>West Salem, WI 54669"
ADDRESS_FULL = "640 Commerce St Suite A, West Salem, WI 54669"

BIO = (
    "Doctor Daniel Eoriatti is a chiropractor at West Salem Chiropractic in West Salem, WI. "
    "He grew up the oldest of 6 children on a pig farm in Iowa. He was introduced to chiropractic care at a very early age. "
    "Farm work took its toll on the body. Dr. Eoriatti found out that chiropractic care was extremely helpful in getting him feeling better "
    "and then keeping him healthy to continue doing the farm work and sports activities throughout his youth.\n"
    "Dr. Eoriatti attended undergraduate school at Loras College in Dubuque, IA. He received his Bachelor of Science Degree and Doctor of Chiropractic Degree "
    "from Palmer College of Chiropractic in Davenport, IA in 1997. Dr. Eoriatti has been in practice helping patients in the area ever since.\n"
    "Over the years, Dr. Eoriatti has seen the benefit and value of chiropractic care and the benefit of what it can do for people. "
    "Dr. Eoriatti treats each patient as an individual not as a number. That is why he schedules his patients on 15 minute blocks to allow enough time "
    "to properly take care of everything that needs to be addressed at your appointment.\n"
    "In utilizing the Gonstead Technique, Dr. Eoriatti takes the time to assess the spine very carefully each and every visit to notice any subtle changes "
    "that may require him to alter the adjustment specifics such as the level adjusted and the direction of the adjustment. In other words, "
    "Dr. Eoriatti's goal is to give you the most specific adjustment possible at your visit to ensure that you get better faster and stay better.\n"
    "Dr. Eoriatti understands that today's insurance coverage does not always cover much of your chiropractic care so he offers affordable price options "
    "for all visit types. Ask how adults can get visits for as little as $30 per visit and children for $25 per visit."
)

QUOTE_EVE = "\u201cVery caring, listens to your needs and promotes things for you to try! Should be voted best place in La Crosse county!\u201d"
QUOTE_BECKY = "\u201cDr. Dan can adjust even the stubborn areas and make an individual feel so much better. He\u2019s an excellent chiropractor!\u201d"

ICON_CLOCK = '<svg class="util__icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M12 7v5l3.5 2" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>'
ICON_PIN = '<svg class="util__icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s7-6.2 7-11.2A7 7 0 0 0 5 9.8C5 14.8 12 21 12 21z" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="9.8" r="2.2" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>'
ICON_PHONE = '<svg class="util__icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M7.2 3.8h3.1l1.2 4.2-2 1.2a12.5 12.5 0 0 0 5.3 5.3l1.2-2 4.2 1.2v3.1c0 .7-.6 1.4-1.4 1.5-7.3.8-13.4-5.3-12.6-12.6.1-.8.8-1.4 1.5-1.4z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>'
ICON_FB = '<svg class="util__icon" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M14.2 21v-7.2h2.4l.4-2.8h-2.8V9.2c0-.8.2-1.4 1.4-1.4h1.5V5.2c-.3 0-1.2-.1-2.3-.1-2.3 0-3.8 1.4-3.8 3.9v2h-2.5v2.8h2.5V21h3.2z"/></svg>'
ICON_ARROW = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 12h10M13 7l5 5-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

G_ICONS = {
    "xrays": '<svg viewBox="0 0 64 64" aria-hidden="true"><rect x="18" y="8" width="28" height="48" rx="2" fill="none" stroke="currentColor" stroke-width="2.4"/><path d="M32 14v36M24 22h16M24 42h16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>',
    "palpation": '<svg viewBox="0 0 64 64" aria-hidden="true"><path d="M20 40c0-8 4-16 12-20" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/><path d="M28 46c2-10 8-18 16-22" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/><circle cx="44" cy="20" r="5" fill="none" stroke="currentColor" stroke-width="2.4"/></svg>',
    "instrumentation": '<svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="16" fill="none" stroke="currentColor" stroke-width="2.4"/><path d="M32 16v-6M32 54v-6M16 32H10M54 32h-6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/><path d="M32 32l9-6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>',
    "visualization": '<svg viewBox="0 0 64 64" aria-hidden="true"><path d="M8 32s10-14 24-14 24 14 24 14-10 14-24 14S8 32 8 32z" fill="none" stroke="currentColor" stroke-width="2.4"/><circle cx="32" cy="32" r="7" fill="none" stroke="currentColor" stroke-width="2.4"/></svg>',
    "case": '<svg viewBox="0 0 64 64" aria-hidden="true"><rect x="14" y="16" width="36" height="36" rx="3" fill="none" stroke="currentColor" stroke-width="2.4"/><path d="M22 28h20M22 36h20M22 44h12" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/><path d="M24 16v-4h16v4" fill="none" stroke="currentColor" stroke-width="2.2"/></svg>',
}


def hours_block():
    return """
    <div class="util__hours">
      <div><span class="d">Monday</span><span>7:30am - 12:00pm, 1:30pm - 5:30pm</span></div>
      <div><span class="d">Tuesday</span><span>3:00pm - 6:30pm</span></div>
      <div><span class="d">Wednesday</span><span>8:00am - 12:00pm, 1:30pm - 5:30pm</span></div>
      <div><span class="d">Thursday</span><span>3:00pm - 6:30pm</span></div>
      <div><span class="d">Friday</span><span>9:00am - 12:00pm, 1:30pm - 4:00pm</span></div>
      <div><span class="d">Saturday</span><span>Closed</span></div>
      <div><span class="d">Sunday</span><span>Closed</span></div>
    </div>
    """


def util_bar():
    return f"""
    <div class="util">
      <div class="util__row wrap">
        <div class="util__item">
          <button class="util__btn" type="button" aria-expanded="false" aria-controls="panel-hours">{ICON_CLOCK} Office Hours</button>
          <div class="util__panel" id="panel-hours">
            <h3>Office Hours</h3>
            {hours_block()}
          </div>
        </div>
        <div class="util__item">
          <button class="util__btn" type="button" aria-expanded="false" aria-controls="panel-visit">{ICON_PIN} Visit Us</button>
          <div class="util__panel" id="panel-visit">
            <h3>Visit Us</h3>
            <p>{ADDRESS_LINES}</p>
            <p><a href="{MAPS}">Directions</a></p>
          </div>
        </div>
        <div class="util__item">
          <a class="util__link" href="tel:{PHONE_TEL}">{ICON_PHONE} {PHONE_DISPLAY}</a>
        </div>
        <div class="util__item util__fb">
          <a class="util__link" href="{FACEBOOK}" aria-label="West Salem Chiropractic on Facebook">{ICON_FB}</a>
        </div>
      </div>
    </div>
    """


def nav(prefix: str, active: str = "home") -> str:
    c = f"{prefix}coming/"
    home_active = "is-active" if active == "home" else ""
    return f"""
    <div class="nav-bar">
      <div class="nav-bar__inner wrap">
        <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav">
          <span class="menu-toggle__icon" aria-hidden="true"><span></span></span> Menu
        </button>
        <ul class="nav" id="site-nav">
          <li><a href="{prefix}" class="{home_active}">Home</a></li>
          <li>
            <button class="nav__top" type="button" aria-expanded="false">About</button>
            <div class="nav__drop">
              <a href="{prefix}meet-the-doctor/">Meet the Doctor</a>
              <a href="{c}">Payment Methods</a>
              <a href="{prefix}testimonials/">Testimonials</a>
              <a href="{c}">Office Tour</a>
            </div>
          </li>
          <li>
            <button class="nav__top" type="button" aria-expanded="false">Patients</button>
            <div class="nav__drop">
              <a href="{c}">Who Was Dr. Gonstead?</a>
              <a href="{c}">5 Components of the Gonstead System</a>
              <a href="{c}">Blog</a>
            </div>
          </li>
          <li>
            <button class="nav__top" type="button" aria-expanded="false">Services</button>
            <div class="nav__drop nav__drop--wide">
              <div>
                <div class="nav__group">Chiropractic Care</div>
                <div class="nav__group">Spine related</div>
                <a href="{c}">Back Pain</a>
                <a href="{c}">Headaches &amp; Migraines</a>
                <a href="{c}">Neck Pain</a>
                <a href="{c}">Sciatica</a>
                <a href="{c}">Scoliosis</a>
                <div class="nav__group">Injuries</div>
                <a href="{c}">Automobile Injury</a>
                <a href="{c}">Disc Injury</a>
                <a href="{c}">Whiplash</a>
                <a href="{c}">Work Injury</a>
              </div>
              <div>
                <div class="nav__group">Extremities</div>
                <a href="{c}">Arm and Leg Pain</a>
                <a href="{c}">Carpal Tunnel</a>
                <a href="{c}">Shoulder Pain</a>
                <div class="nav__group">Family chiropractic</div>
                <a href="{c}">Chiropractic Care for Kids</a>
                <a href="{c}">Pregnancy</a>
                <a href="{c}">Wellness Care</a>
                <a href="{c}">Weight Loss Management</a>
                <a href="{c}">Vertigo</a>
                <a href="{c}">Aspen Laser</a>
                <a href="{c}">Custom Orthotics</a>
                <a href="{c}">The Gonstead System</a>
              </div>
            </div>
          </li>
          <li><a href="{prefix}testimonials/">Review Us</a></li>
          <li><a href="{prefix}contact/">Contact</a></li>
        </ul>
      </div>
    </div>
    """


def sticky_bar(prefix: str) -> str:
    return f"""
    <div class="sticky">
      <div class="sticky__inner">
        <a class="sticky__logo" href="{prefix}"><img src="{prefix}assets/images/logo.png" alt="West Salem Chiropractic"></a>
        <p class="sticky__msg">New patients are welcome. Request a visit or call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>
        <a class="btn" href="{prefix}request/">Request an Appointment {ICON_ARROW}</a>
      </div>
    </div>
    """


def footer(prefix: str) -> str:
    legal = [
        ("accessibility/", "Accessibility"),
        ("anti-discrimination/", "Anti-Discrimination"),
        ("healthcare-disclaimer/", "Healthcare Disclaimer"),
        ("hipaa-notice/", "HIPAA Policy"),
        ("privacy-policy/", "Privacy Policy"),
        ("terms-of-service/", "Terms of Service"),
        ("good-faith-estimate/", "Good Faith Estimate"),
    ]
    links = "\n".join(f'<a href="{prefix}{s}">{t}</a>' for s, t in legal)
    return f"""
    <footer class="footer">
      <div class="wrap">
        <p class="footer__copy">Copyright © 2026 West Salem Chiropractic</p>
        <div class="footer__legal">{links}</div>
        <p class="footer__note">Design preview only. This is not the live West Salem Chiropractic website. Nothing here is published on westsalemchiropractic.com.</p>
      </div>
    </footer>
    """


def wave(fill: str) -> str:
    path = "M0,32 C240,64 480,0 720,24 C960,48 1200,8 1440,32 L1440,64 L0,64 Z"
    return f'<div class="wave" aria-hidden="true"><svg viewBox="0 0 1440 64" preserveAspectRatio="none"><path d="{path}" fill="{fill}"></path></svg></div>'


def head(title: str, desc: str, prefix: str, canonical: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="noindex,nofollow">
  <link rel="canonical" href="{canonical}">
  <link rel="icon" type="image/png" sizes="32x32" href="{prefix}assets/images/favicon-32.png">
  <link rel="apple-touch-icon" href="{prefix}assets/images/favicon-180.png">
  <link rel="stylesheet" href="{prefix}assets/css/fonts.css">
  <link rel="stylesheet" href="{prefix}assets/css/site.css">
</head>
"""


def chrome_open(title, desc, prefix, canonical, active="home"):
    return (
        head(title, desc, prefix, canonical)
        + f"""
<body>
  <div class="preview-banner">Design preview, not live</div>

  <svg class="clip-svg" aria-hidden="true" focusable="false">
    <defs>
      <clipPath id="hexClip" clipPathUnits="objectBoundingBox">
        <path d="M0.28 0.05 Q0.50 0.00 0.72 0.05 L0.95 0.38 Q1.00 0.50 0.95 0.62 L0.72 0.95 Q0.50 1.00 0.28 0.95 L0.05 0.62 Q0.00 0.50 0.05 0.38 Z"/>
      </clipPath>
    </defs>
  </svg>
  <a class="skip" href="#content">Skip to content</a>
  {sticky_bar(prefix)}
  {util_bar()}
  {nav(prefix, active)}
"""
    )


def chrome_close(prefix: str) -> str:
    return footer(prefix) + f"""
  <script src="{prefix}assets/js/site.js"></script>
</body>
</html>
"""


def write(path: Path, html: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html)
    print("wrote", path.relative_to(OUT), "bytes", len(html))


def homepage():
    p = ""
    html = chrome_open(
        "Chiropractor in West Salem, WI | West Salem Chiropractic (Design Preview)",
        "Gonstead chiropractic care with Dr. Daniel Eoriatti in West Salem, Wisconsin. Design preview only. Not the live site.",
        p,
        "/west-salem-chiro-preview-v2/",
        "home",
    )
    html += f"""
  <main id="content">
    <section class="hero">
      <div class="wrap hero__grid">
        <div class="hero__copy">
          <div class="hero__brand">
            <img src="{p}assets/images/logo.png" alt="West Salem Chiropractic">
          </div>
          <h1><span>Care for the cause</span><span class="line2">Not just the pain</span></h1>
          <p class="hero__offer">Ask how you can pay $32 per visit after your first visit! Call today.</p>
          <a class="btn" href="{p}request/">Request an Appointment</a>
        </div>
        <div class="hero__visual">
          <div class="hex hex--placeholder" role="img" aria-label="Photo placeholder: family photo coming">
            <div>
              <strong>Photo placeholder</strong>
              <span>Family photo coming. New photos arrive next week.</span>
            </div>
          </div>
          <div class="hero__band" aria-hidden="true"></div>
        </div>
      </div>
    </section>

    <section class="welcome">
      <div class="wrap welcome__grid">
        <div class="welcome__col">
          <h2>Chiropractor in West Salem</h2>
          <p>West Salem Chiropractic is the Gonstead practice of Dr. Daniel Eoriatti, serving West Salem, Wisconsin and all of La Crosse County. If pain from a car accident, a spinal problem, or pregnancy has been hanging on, there is usually a mechanical reason for it. Dr. Eoriatti looks for that reason and builds a plan around what your exam shows, with a specific adjustment and practical advice you can use the rest of the week.</p>
        </div>
        <div class="welcome__col">
          <h2>A specific, careful approach</h2>
          <p>Dr. Eoriatti specializes in the Gonstead technique. That means visualization, instrumentation, palpation, X-ray, and your symptoms are all considered before an adjustment. The same careful look applies when the problem is back pain, a disc injury, pain that travels into an arm or a leg, or the spinal and pelvic changes of pregnancy. You do not have to wait until the pain is unbearable to come in.</p>
        </div>
      </div>
    </section>

    <section class="cards">
      <div class="wrap cards__grid">
        <a class="card card--doctor" href="{p}meet-the-doctor/">
          <div class="card__img"><img src="{p}assets/images/doctor-formal.jpg" alt="Dr. Daniel Eoriatti at West Salem Chiropractic"></div>
          <div class="card__bar">Meet the Doctor</div>
          <p class="card__note">Read Dr. Eoriatti's story and how he works with each patient.</p>
        </a>
        <a class="card" href="{p}testimonials/">
          <div class="card__img"><img src="{p}assets/images/doctor-spine.jpg" alt="Dr. Eoriatti explaining the spine to a patient"></div>
          <div class="card__bar">Testimonials</div>
          <p class="card__note">Hear from people who have been to this office.</p>
        </a>
        <a class="card" href="{p}contact/">
          <div class="card__img"><img src="{p}assets/images/front-desk.jpg" alt="The front desk at West Salem Chiropractic"></div>
          <div class="card__bar">Contact Us</div>
          <p class="card__note">Call, visit, or send a request. We will help you get started.</p>
        </a>
      </div>
    </section>

    <section class="why" id="why">
      <div class="wrap why__grid">
        <div class="why__photo">
          <div class="hex hex--photo">
            <img src="{p}assets/images/doctor-xray.jpg" alt="Dr. Daniel Eoriatti reviewing spinal X-rays">
          </div>
        </div>
        <div class="why__lists">
          <h2>Why Dr. Daniel Eoriatti?</h2>
          <p class="why__kicker">West Salem, Wisconsin's chiropractor</p>
          <ul>
            <li>Extremity Adjusting - Knees, Shoulders, Ankles, Wrists</li>
            <li>Back Pain Specialist</li>
            <li>Pregnancy Chiropractor</li>
            <li>Spine Injury Professional</li>
            <li>Car Accident Back Pain Chiropractor</li>
            <li>Wound/Injury Healing with Aspen Laser</li>
            <li>Gonstead Technique Expert</li>
            <li>Over 30 Years of Experience</li>
          </ul>
          <div class="insure">
            <h3>Insurances accepted</h3>
            <ul>
              <li>Anthem Blue Cross Blue Shield</li>
              <li>United Healthcare</li>
              <li>The Alliance</li>
              <li>Gundersen Lutheran Health Plan</li>
              <li>Sr. Preferred</li>
              <li>Medicare</li>
              <li>Medicaid</li>
              <li>UMR</li>
            </ul>
            <p class="why__fine">Other options are also available, please call for clarification.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="band">
      <div class="wrap">
        <h2>You deserve to feel better<span class="sub">Over 30 Years of Experience</span></h2>
      </div>
    </section>

    <section class="training">
      <div class="wrap training__grid">
        <div class="training__copy">
          <h2>How are chiropractors qualified?</h2>
          <p>A Doctor of Chiropractic is a four-year doctoral program following undergraduate study, covering anatomy, physiology, diagnosis, imaging and hands-on technique, followed by national board examinations and state licensure. Licensed chiropractors also complete continuing education to stay licensed. In Wisconsin, that includes 40 hours of continuing education every two years.</p>
          <p>When you come to West Salem Chiropractic, the first job is to understand what is going on and whether this office can help. If it can, we will lay out a plan that fits you.</p>
        </div>
        <div class="training__photo">
          <img src="{p}assets/images/clinic-exterior.jpg" alt="The West Salem Chiropractic clinic on Commerce Street">
        </div>
      </div>
    </section>

    <section class="stories" id="stories">
      <div class="wrap stories__grid">
        <div class="stories__photo">
          <img src="{p}assets/images/doctor-casual.jpg" alt="Dr. Daniel Eoriatti at West Salem Chiropractic">
        </div>
        <div>
          <h2>What our patients say</h2>
          <div class="stories__slide">
            <p class="quote">{QUOTE_EVE}</p>
            <p class="quote__who">Eve Z.</p>
          </div>
          <div class="stories__slide" hidden>
            <p class="quote">{QUOTE_BECKY}</p>
            <p class="quote__who">Becky F.</p>
          </div>
          <div class="dots" role="tablist" aria-label="Patient quotes">
            <button type="button" class="is-on" aria-label="Quote from Eve Z." aria-selected="true"></button>
            <button type="button" aria-label="Quote from Becky F." aria-selected="false"></button>
          </div>
        </div>
      </div>
    </section>

    <section class="gonstead" id="gonstead">
      <div class="wrap">
        <h2>Components of the Gonstead System</h2>
        <div class="gonstead__row">
          <div class="gitem">
            <div class="gitem__circle">{G_ICONS['xrays']}</div>
            <div class="gitem__name">X-Rays</div>
            <p class="gitem__blurb">Full-spine films that show contour, posture, and an accurate count of the vertebrae.</p>
          </div>
          <div class="gitem">
            <div class="gitem__circle">{G_ICONS['palpation']}</div>
            <div class="gitem__name">Palpation</div>
            <p class="gitem__blurb">Hands-on static and motion checks for changes in contour, tone, texture, and movement.</p>
          </div>
          <div class="gitem">
            <div class="gitem__circle">{G_ICONS['instrumentation']}</div>
            <div class="gitem__name">Instrumentation</div>
            <p class="gitem__blurb">A dual-probe instrument compares temperature along the spine to help locate irritation.</p>
          </div>
          <div class="gitem">
            <div class="gitem__circle">{G_ICONS['visualization']}</div>
            <div class="gitem__name">Visualization</div>
            <p class="gitem__blurb">Posture and gait are observed from the moment you walk in, then checked against the other findings.</p>
          </div>
          <div class="gitem">
            <div class="gitem__circle">{G_ICONS['case']}</div>
            <div class="gitem__name">Case Management</div>
            <p class="gitem__blurb">Your symptoms are part of the picture, used to pinpoint the area that actually needs the adjustment.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="cta">
      <a class="btn btn--light" href="{p}request/">Request an Appointment {ICON_ARROW}</a>
    </section>

    <section class="visit">
      <div class="wrap">
        <div class="visit__box">
          <h2>West Salem Chiropractic</h2>
          <p>640 Commerce St Suite A<br>West Salem, WI 54669</p>
          <p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
          <a class="visit__maps" href="{MAPS}">Open in Maps</a>
        </div>
        <iframe title="Map of West Salem Chiropractic" src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
    </section>
  </main>
"""
    html += chrome_close(p)
    write(OUT / "index.html", html)


def simple_page(slug: str, title: str, heading: str, body: str, active: str = ""):
    prefix = "../"
    html = chrome_open(
        f"{title} | West Salem Chiropractic (Design Preview)",
        f"{title} at West Salem Chiropractic. Design preview only.",
        prefix,
        f"/west-salem-chiro-preview-v2/{slug}/",
        active,
    )
    html += f"""
  <main id="content">
    <div class="page-hero">
      <div class="wrap">
        <p class="crumb"><a href="{prefix}">Home</a> / {heading}</p>
        <h1>{heading}</h1>
      </div>
    </div>
    <div class="content">
      <div class="wrap">
        {body}
      </div>
    </div>
  </main>
"""
    html += chrome_close(prefix)
    write(OUT / slug / "index.html", html)


def meet_page():
    paras = "".join(f"<p>{p}</p>" for p in BIO.split("\n") if p.strip())
    prefix = "../"
    html = chrome_open(
        "Meet the Doctor | West Salem Chiropractic (Design Preview)",
        "Meet Dr. Daniel Eoriatti of West Salem Chiropractic. Design preview only.",
        prefix,
        "/west-salem-chiro-preview-v2/meet-the-doctor/",
        "about",
    )
    html += f"""
  <main id="content">
    <div class="page-hero">
      <div class="wrap">
        <p class="crumb"><a href="{prefix}">Home</a> / Meet the Doctor</p>
        <h1>Chiropractor Daniel Eoriatti D.C.</h1>
      </div>
    </div>
    <div class="content">
      <div class="wrap training__grid">
        <div class="bio content--narrow">
          {paras}
          <p><a class="btn" href="{prefix}request/">Request an Appointment</a></p>
          <p><a class="btn btn--ghost" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a></p>
        </div>
        <div class="training__photo">
          <img src="{prefix}assets/images/doctor-formal.jpg" alt="Dr. Daniel Eoriatti, D.C.">
        </div>
      </div>
    </div>
  </main>
"""
    html += chrome_close(prefix)
    write(OUT / "meet-the-doctor" / "index.html", html)


def testimonials_page():
    prefix = "../"
    html = chrome_open(
        "Testimonials | West Salem Chiropractic (Design Preview)",
        "Patient testimonials for West Salem Chiropractic. Design preview only.",
        prefix,
        "/west-salem-chiro-preview-v2/testimonials/",
        "about",
    )
    html += f"""
  <main id="content">
    <div class="page-hero">
      <div class="wrap">
        <p class="crumb"><a href="{prefix}">Home</a> / Testimonials</p>
        <h1>Chiropractic Testimonials</h1>
      </div>
    </div>
    <div class="content">
      <div class="wrap content--narrow">
        <blockquote>
          <p class="quote">{QUOTE_EVE}</p>
          <p class="quote__who">Eve Z.</p>
        </blockquote>
        <blockquote>
          <p class="quote">{QUOTE_BECKY}</p>
          <p class="quote__who">Becky F.</p>
        </blockquote>
        <p><a class="btn" href="{prefix}request/">Request an Appointment</a></p>
      </div>
    </div>
  </main>
"""
    html += chrome_close(prefix)
    write(OUT / "testimonials" / "index.html", html)


def contact_page():
    prefix = "../"
    html = chrome_open(
        "Contact | West Salem Chiropractic (Design Preview)",
        "Contact West Salem Chiropractic in West Salem, WI. Design preview only.",
        prefix,
        "/west-salem-chiro-preview-v2/contact/",
        "contact",
    )
    html += f"""
  <main id="content">
    <div class="page-hero">
      <div class="wrap">
        <p class="crumb"><a href="{prefix}">Home</a> / Contact</p>
        <h1>Contact Us</h1>
      </div>
    </div>
    <div class="content">
      <div class="wrap training__grid">
        <div>
          <p>Call the office, stop by, or send a request for a visit. The phone number is a tap-to-call link.</p>
          <p><strong>West Salem Chiropractic</strong><br>{ADDRESS_LINES}<br><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
          <p><a href="{MAPS}">Get directions</a></p>
          <h2>Hours</h2>
          {hours_block()}
          <p style="margin-top:24px"><a class="btn" href="{prefix}request/">Request an Appointment</a></p>
        </div>
        <div>
          <iframe title="Map of West Salem Chiropractic" src="{MAP_EMBED}" loading="lazy" style="width:100%;height:360px;border:0" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
      </div>
    </div>
  </main>
"""
    html += chrome_close(prefix)
    write(OUT / "contact" / "index.html", html)


def request_page():
    prefix = "../"
    html = chrome_open(
        "Request an Appointment | West Salem Chiropractic (Design Preview)",
        "Request an appointment at West Salem Chiropractic. Design preview only. The form is not sent.",
        prefix,
        "/west-salem-chiro-preview-v2/request/",
        "contact",
    )
    html += f"""
  <main id="content">
    <div class="page-hero">
      <div class="wrap">
        <p class="crumb"><a href="{prefix}">Home</a> / Request an Appointment</p>
        <h1>Request an Appointment</h1>
      </div>
    </div>
    <div class="content">
      <div class="wrap">
        <p>The fastest way to get on the schedule is to call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>
        <p>This is a design preview. The form below is not sent.</p>
        <form class="form" id="request-form" action="#" method="post" novalidate>
          <div>
            <label for="request-form-name">Name</label>
            <input id="request-form-name" name="name" type="text" autocomplete="name" required>
          </div>
          <div>
            <label for="request-form-phone">Phone</label>
            <input id="request-form-phone" name="phone" type="tel" autocomplete="tel" required>
          </div>
          <div>
            <label for="request-form-email">Email</label>
            <input id="request-form-email" name="email" type="email" autocomplete="email">
          </div>
          <div>
            <label for="request-form-msg">How can we help?</label>
            <textarea id="request-form-msg" name="message"></textarea>
          </div>
          <button class="btn" type="submit">Send request</button>
        </form>
        <div class="form-note" id="form-preview-note" hidden tabindex="-1">This is a design preview. The form was not sent. Please call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> to request a visit.</div>
      </div>
    </div>
  </main>
"""
    html += chrome_close(prefix)
    write(OUT / "request" / "index.html", html)


def coming_page():
    body = """
      <div class="stub">
        <p>This mockup is the homepage, built to follow the look and section order of the current site, with our own wording. Inner service and condition pages will be part of the full site build.</p>
        <p><a class="btn" href="../">Back to the homepage</a></p>
      </div>
    """
    simple_page("coming", "Inner pages coming", "This page is next", body)


def legal_pages():
    data = json.loads(LEGAL_SRC.read_text())
    tokens = {
        "{{clinic_name}}": "West Salem Chiropractic",
        "{{address_full}}": ADDRESS_FULL,
        "{{address_state}}": "WI",
        "{{phone}}": PHONE_DISPLAY,
        "{{site_url}}": "https://www.westsalemchiropractic.com/",
    }
    for page in data["pages"]:
        html_body = page["html"]
        for k, v in tokens.items():
            html_body = html_body.replace(k, v)
        body = f'<div class="legal-body">{html_body}</div>'
        simple_page(page["slug"], page["title"], page["title"], body)


def extras():
    (OUT / ".nojekyll").write_text("")
    (OUT / "robots.txt").write_text("User-agent: *\nDisallow: /\n")
    (OUT / "README.md").write_text(
        """# West Salem Chiropractic homepage mockup (v2)

Design preview only. Not the live site. Not for indexing.

Homepage mockup for West Salem Chiropractic (Dr. Daniel Eoriatti, West Salem, WI). The layout follows the current site at westsalemchiropractic.com (section order, overall styling) with our own wording and typographic refinements. This replaces the earlier Spine Design-style preview, which stays untouched at https://localember.github.io/west-salem-chiro-preview/.

Every page is served with `noindex,nofollow`. `robots.txt` disallows `/`. A banner on every page says this is a design preview, not live.

Nothing here is published on westsalemchiropractic.com.

Preview: https://localember.github.io/west-salem-chiro-preview-v2/
"""
    )


def main():
    homepage()
    meet_page()
    testimonials_page()
    contact_page()
    request_page()
    coming_page()
    legal_pages()
    extras()
    print("build complete")


if __name__ == "__main__":
    main()
