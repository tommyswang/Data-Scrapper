function apiCall(data) {
    let value = data.getElementsByTagName('input').api_url.value;
    if( value === "" ) {
        alert("Search Field is Empty");
        return false;
    } else {
          try {
            new URL(value);
                      return true;
          } catch (_) {
            alert("Invalid URL");
            return false;
          }
    }
}