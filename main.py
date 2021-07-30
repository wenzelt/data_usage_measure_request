# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests


def header_size(headers):
    return sum(len(key) + len(value) + 4 for key, value in headers.items()) + 2


def get_response_sizes(url: str):
    r = requests.get(url)
    request_line_size = len(r.request.method) + len(r.request.path_url) + 12
    request_size = (
            request_line_size
            + header_size(r.request.headers)
            + int(r.request.headers.get("content-length", 0))
    )
    response_line_size = len(r.reason) + 15
    response_size = (
            response_line_size
            + header_size(r.headers)
            + int(r.headers.get("content-length", 0))
    )
    return {"response_size": response_size, "request_size": request_size}


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    booking_pricing_page = (
        "https://www.booking.com/hotel/de/krone-hirschberg"
        "-grosssachsen.en-gb.html?aid=304142;label=gen173nr-"
        "1FCAEoggI46AdIM1gEaDuIAQGYAQm4ARfIAQzYAQHoAQH4AQuIA"
        "gGoAgO4ApfskIgGwAIB0gIkMTQ5ZDkzZDktNTEzZS00OWI5LWEwY"
        "TUtM2JhNWY2MDhkNWVi2AIG4AIB;sid=9750ec5321b3d587bfdbc7"
        "0e03f4441c;all_sr_blocks=7181001_329605560_0_41_0%2C"
        "7181001_329605560_0_41_0;checkin=2021-08-19;checkout="
        "2021-08-20;dest_id=900039464;dest_type=city;dist=0;"
        "group_adults=2;group_children=0;hapos=1;"
        "highlighted_blocks=7181001_329605560_0_41_0%"
        "2C7181001_329605560_0_41_0;hp_group_set=0;hpos=1;"
        "no_rooms=1;room1=A%2CA;sb_price_type=total;sr_order=popularity;"
        "sr_pri_blocks=7181001_329605560_0_41_0__6500%2C7181001_329605560_0_41_0__6500;"
        "srepoch=1627666195;srpvid=23a87b09b9060278;type=total;ucfs=1&#hotelTmpl"
    )
    booking_search_page_url = "https://www.booking.com/searchresults.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaDuIAQGYATG4AQfIAQzYAQHoAQH4AQKIAgGoAgO4Aq7biogGwAIB0gIkNjlmOWJiNmEtMWNmMC00ZmRhLTgwOTItNmFkMzI4YWEwOWQ32AIF4AIB&sid=1c6d3bb1859e5e59eaf13e16a331d841&tmpl=searchresults&checkin_month=8&checkin_monthday=5&checkin_year=2021&checkout_month=8&checkout_monthday=6&checkout_year=2021&city=-1884892&class_interval=1&dest_id=-1884892&dest_type=city&dtdisc=0&from_sf=1&group_adults=1&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&postcard=0&raw_dest_type=city&room1=A&sb_price_type=total&shw_aparth=1&slp_r_match=0&src=searchresults&srpvid=e7c65f39cf52016f&ss=Weinheim&ss_all=0&ssb=empty&sshis=0&ssne=Weinheim&ssne_untouched=Weinheim&top_ufis=1&nflt=mealplan%3D1%3B&rsf=&track_hp_back_button=1#hotel_63055-back"
    booking_search_page_url_hamburg = "https://www.booking.com/searchresults.html?label=gen173nr-1FCAQoggJCDWNpdHlfLTE3NjExMjNIMVgEaDuIAQGYATG4AQfIAQzYAQHoAQH4AQOIAgGoAgO4AqvRiogGwAIB0gIkODZhODRkOTktZWI4MC00NzYxLWFjYWEtYjNiODhiMjZmYzE12AIF4AIB&sid=a24b923a4c9e2800cd6aa9891b35e79a&sb=1&src=searchresults&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fsearchresults.html%3Flabel%3Dgen173nr-1FCAQoggJCDWNpdHlfLTE3NjExMjNIMVgEaDuIAQGYATG4AQfIAQzYAQHoAQH4AQOIAgGoAgO4AqvRiogGwAIB0gIkODZhODRkOTktZWI4MC00NzYxLWFjYWEtYjNiODhiMjZmYzE12AIF4AIB%3Bsid%3Da24b923a4c9e2800cd6aa9891b35e79a%3Btmpl%3Dsearchresults%3Bcheckin_month%3D8%3Bcheckin_monthday%3D19%3Bcheckin_year%3D2021%3Bcheckout_month%3D8%3Bcheckout_monthday%3D20%3Bcheckout_year%3D2021%3Bcity%3D-1761123%3Bclass_interval%3D1%3Bdest_id%3D-1761123%3Bdest_type%3Dcity%3Bdtdisc%3D0%3Bfrom_sf%3D1%3Bgroup_adults%3D2%3Bgroup_children%3D0%3Binac%3D0%3Bindex_postcard%3D0%3Blabel_click%3Dundef%3Bno_rooms%3D1%3Boffset%3D0%3Bpostcard%3D0%3Broom1%3DA%252CA%3Bsb_price_type%3Dtotal%3Bshw_aparth%3D1%3Bslp_r_match%3D0%3Bsrc%3Dsearchresults%3Bsrc_elem%3Dsb%3Bsrpvid%3D2bd89a4b2e700245%3Bss%3DHamburg%3Bss_all%3D0%3Bssb%3Dempty%3Bsshis%3D0%3Bssne%3DDortmund%3Bssne_untouched%3DDortmund%3Btop_ufis%3D1%26%3B&ss=Hamburg%2C+Hansestadt+Hamburg%2C+Germany&is_ski_area=&ssne=Dortmund&ssne_untouched=Dortmund&city=-1761123&checkin_year=2021&checkin_month=8&checkin_monthday=19&checkout_year=2021&checkout_month=8&checkout_monthday=20&group_adults=2&group_children=0&no_rooms=1&from_sf=1&ss_raw=Hamburg&ac_position=0&ac_langcode=en&ac_click_type=b&dest_id=-1785434&dest_type=city&iata=HAM&place_id_lat=53.549999&place_id_lon=10&search_pageview_id=2bd89a4b2e700245&search_selected=true&search_pageview_id=2bd89a4b2e700245&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0&sb_changed_destination=1"
    pricing_size = get_response_sizes(booking_pricing_page)
    search_page_size = get_response_sizes(booking_search_page_url)
    search_page_size_hamburg = get_response_sizes(booking_search_page_url)
    1 + 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
