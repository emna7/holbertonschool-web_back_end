export default function handleResponseFromAPI(promise) {
  promise.then(() => {
    console.log('Got a response from the API');
    return {
      status: 200,
      body: 'success',
    };
  })
    .then(() => {
      console.log('Got a response from the API');
      return Error();
    })
    .catch('Got a response from the API');
}
