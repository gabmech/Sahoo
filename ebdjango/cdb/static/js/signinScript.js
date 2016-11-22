
	function signOut() {
	    var auth2 = gapi.auth2.getAuthInstance();
	    auth2.signOut().then(function () {
	      console.log('User signed out.');
		  //document.getElementById("signout_button").style.visibility="hidden";
		  //document.getElementById("sign_in_button").style.visibility="visible";
		  //document.getElementById("logged_in").style.visibility="hidden";
		  document.getElementById("signout_button").style.display="none";
		  document.getElementById("sign_in_button").style.visibility="visible";
		  document.getElementById("logged_in").style.display="none";
		    });
	};
		
	function onSignIn(googleUser) {
		  console.log('User signed out.');
		  var profile = googleUser.getBasicProfile();
		  document.getElementById("logged_in").innerHTML="Logged in as " + profile.getName();// + " (" + profile.getGivenName() + profile.getFamilyName() + profile.getEmail() + ") " + profile.getId();
		  //document.getElementById("signout_button").style.visibility="visible";
		  //document.getElementById("sign_in_button").style.visibility="hidden";
		  //document.getElementById("logged_in").style.visibility="visible";
		  document.getElementById("signout_button").style.display="inline";
		  document.getElementById("sign_in_button").style.visibility="hidden"
		  document.getElementById("logged_in").style.display="inline";

	};