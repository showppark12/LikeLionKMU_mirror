import React from "react";

import Container from "@material-ui/core/Container";
import Grid from "@material-ui/core/Grid";

import lion_logo from "./main/lion_logo.png";
import facebook_logo from "./main/facebook_logo.png";

const Footer = () => (
  <footer className="footer">
    <Container maxWidth="lg">
      <Grid container spacing={3}>
        <Grid item sm={3} xs={2}></Grid>
        <Grid item sm={3} xs={4} className="left-footer">
        <table>
          <tr>
            <th><p>CONTACT</p></th>
          </tr>
          <tr>
            <th>
              <a href="https://likelion.net/">
                <img
                  src={lion_logo}
                  alt="lion로고"
                  // style={{ width: "40%", padding: "5px" }}
                />
              </a>
              <a href="https://www.facebook.com/LikeLionKookmin/">
                <img
                  src={facebook_logo}
                  alt="페북로고"
                  // style={{ width: "42%", padding: "5px" }}
                />
              </a>
            </th>
          </tr>
        </table>
        </Grid>
        <Grid item sm={3} xs={4} className="right-footer">
          <p>20707 서울특별시 성북구 정릉로 77 국민대학교</p>
          <br />
          <p>Email kmu@likelion.org</p>
          <p>COPYRIGHT © 2020 KMU-LIKELION.</p>
          <p>ALL RIGHTS RESERVED</p>
        </Grid>
        <Grid item sm={3} xs={2}></Grid>
      </Grid>
      <br />
      <br />
    </Container>
  </footer>
);

export default Footer;