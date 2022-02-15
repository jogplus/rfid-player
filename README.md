# rfid player

Ref:
https://www.reddit.com/r/shortcuts/comments/9hy7oy/shortcuts_my_collection_of_roku_external_control/
https://developer.roku.com/docs/developer-program/debugging/external-control-api.md
https://pimylifeup.com/raspberry-pi-rfid-rc522/
https://spotipy.readthedocs.io/

```
curl "http://192.168.0.25:8060/query/apps"
<?xml version="1.0" encoding="UTF-8" ?>
<apps>
	<app id="31012" type="menu" version="2.0.53">Vudu Movie &amp; TV Store</app>
	<app id="tvinput.hdmi1" type="tvin" version="1.0.0">Chromecast</app>
	<app id="tvinput.hdmi2" type="tvin" version="1.0.0">Nintendo Switch</app>
	<app id="tvinput.dtv" type="tvin" version="1.0.0">Live TV</app>
	<app id="12" type="appl" version="5.1.98088464">Netflix</app>
	<app id="13" type="appl" version="12.3.2021122417">Prime Video</app>
	<app id="2285" type="appl" version="6.57.0">Hulu</app>
	<app id="61322" type="appl" version="52.5.18">HBO Max</app>
	<app id="291097" type="appl" version="1.18.2022020801">Disney Plus</app>
	<app id="151908" type="appl" version="6.0.15">The Roku Channel</app>
	<app id="41468" type="appl" version="2.17.1">Tubi - Free Movies &amp; TV</app>
	<app id="31440" type="appl" version="6.4.20220124">Paramount Plus</app>
	<app id="551012" type="appl" version="8.1.77">Apple TV</app>
	<app id="837" type="appl" version="2.21.94005088">YouTube</app>
	<app id="259656" type="appl" version="1.1.0">Web Video Caster - Receiver</app>
	<app id="22297" type="appl" version="2.8.102">Spotify Music</app>
	<app id="245028" type="appl" version="2.15.0">NBC 5 Chicago</app>
	<app id="195316" type="appl" version="2.21.94005571">YouTube TV</app>
</apps>
```
