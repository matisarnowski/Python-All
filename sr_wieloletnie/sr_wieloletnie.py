sr_wieloletnie_max = {12.8: "styczeń", 17.1: "luty", 21.5: "marzec", 28.9: "kwiecień", 32.3: "maj", 35.5: "czerwiec",
                      37.9: "lipiec", 37.5: "sierpień", 31.1: "wrzesień", 25.6: "październik", 17.4: "listopad", 13.2: "grudzień"}
sr_wieloletnie_sr = {"styczeń": 3.9, "luty": 5.3, "marzec": 6.7, "kwiecień": 12.4, "maj": 17.5, "czerwiec": 18.8,
                     "lipiec": 23.0, "sierpień": 21.1, "wrzesień": 16.9, "październik": 12.1, "listopad": 6.5, "grudzień": 4.6}
print("Średnia temparatura w miesiącu dla, którego średnia wieloletnia temparatura była najwyższa, to: ",
      sr_wieloletnie_sr[sr_wieloletnie_max[max(sr_wieloletnie_max)]], " i jest to miesiąc: ", sr_wieloletnie_max[max(sr_wieloletnie_max)], '.')
