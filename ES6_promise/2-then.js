export default function handleResponseFromAPI(promise) {
  console.log('Got a response from the API');
  return promise
    .then(() => ({ status: 200, body: 'success' }))
    .catch(() => new Error());
}
