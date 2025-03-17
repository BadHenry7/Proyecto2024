import { redirect } from '@sveltejs/kit';
import { OAuth2Client } from 'google-auth-library';
import {SECRET_CLIENT_ID,SECRET_CLIENT_SECRET} from '$env/static/private';
import {MICROSOFT_CLIENT_ID, MICROSOFT_CLIENT_SECRET} from '$env/static/private';
console.log("verificando")


export const actions = {
    OAuth2: async({})=>{
        const redirectURL = 'http://localhost:5173/oauth';

        console.log('id',SECRET_CLIENT_ID)

        const oAuth2Client = new OAuth2Client(
            SECRET_CLIENT_ID,
            SECRET_CLIENT_SECRET,
            redirectURL
          );
      
          // Generate the url that will be used for the consent dialog.
          const authorizeUrl = oAuth2Client.generateAuthUrl({
            access_type: 'offline',
            scope: 'https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email openid ',
            prompt: 'consent'
          });
          console.log("------  ----   --   ", authorizeUrl)
          throw redirect(302,authorizeUrl);
    },


      OAuth2Microsoft: async () => {


        console.log(MICROSOFT_CLIENT_ID)
        console.log(MICROSOFT_CLIENT_SECRET)
      const redirectURL = 'http://localhost:5173/oauth-microsoft';

      const authorizeUrl = `https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=${MICROSOFT_CLIENT_ID}&response_type=code&redirect_uri=${redirectURL}&scope=openid email profile User.Read&response_mode=query&prompt=consent`;



      throw redirect(302, authorizeUrl);
  }

}