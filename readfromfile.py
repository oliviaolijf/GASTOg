import io

openFile = "data\\system.txt"

with open(openFile, 'r') as file:
    # alle regels worden lijn per lijn afgegaan
    content = file.readlines()
    # loop door alle regels 1 per 1
    for i in content:
        ifEmpty = False
        if i == "\n":
            ifEmpty = True
        linePerLine = i

        if ifEmpty == False:
            # splits alle delen en verwijder de ""
            parts = linePerLine.split('"')

            # als de lijn start met film spring dan in de if statement
            if parts[0].split()[0] == "film":

                # verwijder de film gedeelte van de it
                parts[0] = parts[0].split()[-1]

                # stel alle gesplitste delen op met de overeenkomstige stukken
                id = parts[0]
                title = parts[1]
                rating = parts[2].strip()

                samen = [id,title,rating]

                # print het resultaat
                print(samen)

            # als de lijn start met gebruiker spring dan in de if statement
            if parts[0].split()[0] == "gebruiker":

                parts = linePerLine.split()

                # stel alle gesplitste delen op met de overeenkomstige stukken
                id = parts[1]
                voornaam = parts[2]
                achternaam = parts[3]
                email = parts[4]

                samen = [id,voornaam,achternaam,email]

                # print het resultaat
                print(samen)

            if parts[0].split()[0] == "zaal":

                parts = linePerLine.split()

                # stel alle gesplitste delen op met de overeenkomstige stukken
                zaalnummer = parts[1]
                overigePlaatsen = parts[2]

                samen = [zaalnummer,overigePlaatsen]

                # print het resultaat
                print(samen)

            if parts[0].split()[0] == "vertoning":

                parts = linePerLine.split()

                id = parts[1]
                zaalnummer = parts[2]
                slot = parts[3]
                datum = parts[4]
                filmid = parts[5]
                vrijePlaatsen = parts[6]

                samen = [id,zaalnummer,slot,datum,filmid,vrijePlaatsen]

                # print het resultaat
                print(samen)

            if len(parts[0].split()[0]) == 10 and parts[0].split()[0][4] == '-':

                parts = linePerLine.split()

                if len(parts) != 3:

                    datum = parts[0]
                    tijd = parts[1]
                    user = parts[3]
                    vertoning = parts[4]
                    if len(parts) == 6:
                        ticketten = parts[5]
                        samen = [datum, tijd, user, vertoning, ticketten]
                    else:
                        samen = [datum, tijd, user, vertoning, 1]

                    print(samen)

            if len(parts[0].split()[0]) == 10 and parts[0].split()[0][4] == '-':

                parts = linePerLine.split()

                if len(parts) == 3:
                    logDatum = parts[0]
                    logTijd = parts[1]
                    
                    samen = [logDatum, logTijd]

                    # print het resultaat
                    print(samen)


with io.open('example.html', mode='w') as file:
    file.write("""<!DOCTYPE html>
<html>
  <head>
    <style>
      body {
        height: 100%;
        margin: 0;
        padding: 0;
        background-color: #ffffff;
        overflow-y: scroll;
      }

      .top-bar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 70px;
        background-color: #3782a3;
        z-index: 3;
      }

      .bottom-bar {
        position: fixed;
        top: 70px;
        left: 0;
        width: 100%;
        height: 190px;
        background-color: #064460;
        z-index: 1;
      }

      .bottom-bar.fadeout {
        opacity: 0;
        transition: opacity 0.5s ease-in-out;
      }

      #content {
        height: calc(100vh - 260px);
        overflow-y: scroll;
        padding: 20px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
      }

      .vertical-bar {
        position: absolute;
        top: 0;
        bottom: 0;
        min-width: 225px;
        margin: auto;
        background-color: #4a4a4a;
        background-size: cover;
        z-index: 2;
      }

      .vertical-bar.left {
        left: 18.3%;
        transform: translateX(-50%);
      }

      .vertical-bar.right {
        right: 18.3%;
        transform: translateX(50%);
      }

      .menu-bar {
        font-family: Arial, sans-serif;
        font-size: 14px;
        font-weight: bold;
        position: absolute;
        top: calc(50% + 2px);;
        transform: translateY(-50%);
        left: calc(18.3% + 225px - 92px); /* adjust the 10px value to your preference */
        background-color: #064460;
        color: #ffffff;
        padding: 9px 19px;
        border-radius: 0px;
        cursor: pointer;
      }

        .menu-bar:hover {
        background-color: #064460;
        color: #ffffff;

      }

      table {
        border-collapse: collapse;
        margin-top: 20px;
        border: 1px solid black;
        text-align: center;
      }

      td, th {
        border: 1px solid black;
        text-align: center;
      }

      h1 {
        text-align: center;
      }
    </style>
    <script>
      window.onload = function() {
      document.querySelector('.menu-bar').addEventListener('click', function() {
       location.reload();
        });
      });
    </script>
  </head>
  <body>
    <div class="top-bar">
      <div class="menu-bar">MENU</div>
    </div>
    <div class="bottom-bar"></div>
    <div class="vertical-bar left"></div>
    <div class="vertical-bar right"></div>
    <div id="content">
		<h1>Log op 2023-10-10 18:00</h1>
		<table>
			<thead>
				<tr>
					<th>Datum</th>
					<th>Film</th>
					<th>14:30</th>
					<th>17:00</th>
					<th>20:00</th>
					<th>22:30</th>
				</tr>
			</thead>
			<tbody>
				<tr>
					<td>2023-10-10</td>
					<td></td>
					<td>F:10</td>
					<td>W:2</td>
					<td>G:0</td>
					<td></td>
				</tr>
			</tbody>
		</table>
    </div>
  </body>
</html>
""")
    file.close()