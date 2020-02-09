import axios from "axios";
import { tokenConfig } from "./api_auth";
axios.defaults.baseURL = "http://127.0.0.1:8000/";

export default {
  /* Board CRUD api */
  //모든글 불러오기
  getAllPosts(url) {
    console.log("getAllPosts 실행.");
    return axios.get(`Board/${url}/`, tokenConfig());
  },
  //단일 글 불러오기 및 단일댓글 불러오기?
  getPost(url, id) {
    console.log("getPost 실행");
    return axios.get(`Board/${url}/` + String(id), tokenConfig());
  },

  //글 생성
  createPost(url, data) {
    console.log("createPost 실행.");
    return axios.post(`Board/${url}/`, data, tokenConfig());
  },

  //글 수정
  updatePost(url, id, data) {
    console.log("updatePost 실행.");
    return axios.put(`Board/${url}/` + String(id) + "/", data, tokenConfig());
  },

  //글 삭제
  deletePost(url, id) {
    console.log("deletePost 실행.");
    return axios.delete(`Board/${url}/` + String(id), tokenConfig());
  },

  //댓글 불러오기
  getComments(url, id) {
    console.log("getComments 실행.");
    return axios.get(`Board/${url}/?search=` + String(id), tokenConfig());
  },

  //현재 like 상태 get
  getScrap(id) {
    console.log("get scrap api 실행.");
    return axios.get(`Board/board/${id}/get_scrap`, tokenConfig());
  },
  //like 상태 변경요청.
  changeScrap(id) {
    console.log("change scrap status api 실행.");
    return axios.get(`Board/board/${id}/change_scrap`, tokenConfig());
  }
};
