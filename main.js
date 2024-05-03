const fs = require('fs');

const now = Date.now() / 1000;

fs.readFile('last_call.txt', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  const t_i = parseFloat(data);
  const timeElapsed = (now - t_i) / 60;

  if (timeElapsed > 5) {
    const axios = require('axios');
    const apiUrl = 'https://discord.com/api/webhooks/1235427298971353130/oC3htsYrqPtUZ9DMHuY60zL9QnTIfJoscvtg6JKFsYxvl310-AJUKhVFb1UR7g0pJHLT';

    axios.get(apiUrl)
      .then((response) => {
        const message = response.data;
        message.content = `Hi <@&1134833719493005352>! Rye's laptop has stopped responding in the last ${Math.round(timeElapsed - 0.5)} minutes - could be power outage, internet outage, who knows. Kindly message them by [Messenger](https://m.me/nokay.rra) to find out more.`;
        axios.post(apiUrl, message)
          .then(() => {
            console.log('Message sent successfully');
          })
          .catch((error) => {
            console.error('Error sending message:', error);
          });
      })
      .catch((error) => {
        console.error('Error fetching message:', error);
      });
  } else {
    fs.writeFile('last_call.txt', now.toString(), (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});

