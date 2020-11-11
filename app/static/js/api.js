function apiCall(data) {
    let structured = data.getElementsByTagName('input').structured;
    let value = data.getElementsByTagName('input').api_url.value;
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
          if(structured.checked) {
              structured.value = "structured";
          } else {
              data.getElementsByTagName('input').flat.value = "flat";
          }
          return true;
    }
}