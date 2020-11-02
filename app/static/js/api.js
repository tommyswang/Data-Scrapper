function apiCall(data) {
    let value = data.getElementsByTagName('input')[0].value;
    if( value === "" ) {
        alert("Search Field is Empty");
        return false;
    } else {
          try {
            new URL(value);
          } catch (_) {
            alert("Invalid URL");
            return false;
          }
          return true;
    }
    return false;
}