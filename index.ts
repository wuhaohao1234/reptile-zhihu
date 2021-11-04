const response = await fetch(
  "https://www.zhihu.com/api/v3/feed/topstory/hot-list-web?limit=50&desktop=true",
);
const result = await response.json()

console.log(result);

