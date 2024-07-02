from ytapi.oauth_runnor import OAuthRunnor


def main():
    runnor = OAuthRunnor()
    # runnor.show_default_channel_info()
    # name = 'beating'
    name = 'flyswamp'
    # name = 'nature_forest'
    runnor.upload_ytdl(name)
    # runnor.delete_ytdl('beating')


if __name__ == "__main__":
    main()


#1  gisselfeld_fireworks           Gisselfelds fyrværkeri, der bortjager tusindvis af fugle.
#2  beating                        Slåning af Søtorup-enge.avi
#3  feb2011                        feb2011.AVI
#4  nielstrup1970                  Nielstrup Sø cirka 1970
#5  flyswamp                       Filmoptagelse fra fly over Holmegaard Mose
#6  nature_forest                  Sjælden filmoptagelse af forsvunden naturskov
#7  mouse_awake                    Musvåge fanget i fælde sættes fri
#8  Gisselfeld_abuse_1             Gisselfelds mishandlede landbrugsjorder (video nr.1)
#9  Gisselfeld_abuse_2             Gisselfelds mishandlede landbrugsjorder (video nr. 2)
#10 Gisselfeld_ratproblem          Gisselfelds jagtforretning skaber rotteproblemer
#11 Gisselfeld_destroy_deep_lake   Gisselfeld ødelægger Sjællands næstdybeste sø
