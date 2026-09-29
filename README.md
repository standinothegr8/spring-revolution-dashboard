# Spring Revolution Dashboard — Streamlit deployment

Workshop companion for *Recalibrating the Spring Revolution*. The dashboard is a
single self-contained HTML page (`assets/dashboard.html`); `app.py` serves it
through Streamlit so it can live on Streamlit Community Cloud or any server that
runs Python.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Open http://localhost:8501. Add `?tab=ground` (or `timeline`, `actors`, `means`,
`tensions`, `scenarios`, `recalibrate`) to open a section directly.

## Deploy on Streamlit Community Cloud (free)

1. Push this folder to a GitHub repository (public or private).
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click **New app**, choose the repository, branch `main`, main file `app.py`.
4. Click **Deploy**. The app gets a URL like
   `https://<your-name>-spring-revolution.streamlit.app`.

Every push to the branch redeploys automatically.

## Updating the figures

All numbers, timeline events, actor notes and sources are defined in
`assets/dashboard.html`. Search for the value (for example `8,420`) and the
`data` arrays near the bottom of the file (`EV`, `AC`, `RG`, `POL`, `SIGNS`,
`CQ`, `FL`). Change the "Figures as of" date in the header when you do.

## Notes

- Per-viewer state (sliders, calibration guesses, added assumptions) is kept in
  each visitor's browser and is not shared or sent anywhere.
- On Streamlit 1.60+ the frame sizes itself to the page. On older releases the
  fixed `FRAME_HEIGHT` in `app.py` applies; raise it if the page clips.
- Fonts load from Google Fonts; the page falls back to system fonts offline.
