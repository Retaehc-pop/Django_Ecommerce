import React from "react";

export async function getStaticPaths() {
  const paths = await getAllCategories();
  return {
    paths,
    fallback: false,
  };
}

export async function getStaticProps({ params }) {
  const res = await fetch("http://127.0.0.1:8000/api/category/" + params.slug);
  const posts = await res.json();

  return {
    props: {
      posts,
    },
  };
}

export default function Category({ posts }) {}
