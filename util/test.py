import face_recognition_util
import cv2
import base64
from datetime import datetime

print("开始识别人脸")
start_time = datetime.now()
base64_code = "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofH""h0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyM" \
              "jIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAC4AJYDASIA" \
              "AhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF" \
              "9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0" \
              "RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztL" \
              "W2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBA" \
              "QAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEI" \
              "FEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hp" \
              "anN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1db" \
              "X2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD38dKKB0ooAKKKKACiiigAoqK4uYbWF" \
              "pZpFRFGSzHAFeXeJvjDbWU7W+jxrdOpw0hOF/D1pXGkeq5HqKNw9RXzdd/FHXblmZpkjycgRg8VWh+I+v" \
              "RE/wClMyn+FucUXHY+m6K8D0n4t6hCrR3J3jGVOeRXa+HPinZakoS7xG+QCfrRzCsej0VFb3MN1GJIZFdT" \
              "3BqWmIKKKKACiiigAooooAB0ooHSigAooooAKzda1u00Owku7t9qIM1Zv7yOxs5Z5WCqik5Jr5u8aeML/wA" \
              "RahJE8x+xxMfLRTx9fek30KSuTeMviDqHiKWSFJGisQfljAwWHvXDtIx6cUSMSeaRVLAgck0hjCx7Umc8k1P" \
              "5Q288Huab5J3ZFO4rDFI+lSI7Icq2PxpfL52gH3JqMggYpDPRvA/xBl8OyCG68ye0Y5IzyvqRXvGj6xaa3p0d7" \
              "ZyB43GfcfWvkaKTB56V2Hgrxne+HNSTbITZMf3sTNwfcUk7A1c+maKr2F5Hf2UV1EwKSKGBHvVirICiiigAoooo" \
              "AB0ooHSigAoopGOFJ9BQB5b8X9eEFrBpMEuJZjukA7LXikkeSR6muo8aXR1DxnfSh2ZEfaN3tVC1057u6ARcip8zV" \
              "LSyOf8As7O54PWtbT9Ge4bhfYf1rrbHwq5Ad1Ayc5rorLSYbJRhcn1NZTm7aG0KavqcA3hydpAkaEt344qxbeDriT5pCE" \
              "9q9C8lFHCgfSmbTnj8ax5pW3NuWN72OWi8JWwUIy59SaW48H2LptWMD3FdSoJJFGw+lZPm7l6Hlep+Frq1ctFETH25BrD5" \
              "ilKupXHWva5YVdChHWuA8VaJ5S/aIxk55xWtOs72kY1KSteJ6n8ItdW+0JtPY/vLY4Hupr0ivmP4calNp/jKyVGIWVvLcD" \
              "uCK+mwcgGuuJxyQtFFFUSFFFFAAOlFA6UUAFRXOfssuOu01LTJV3RMvqKAPmMwS32rzxKm5zMQQB1Oa9G0vSINNg3MFL45" \
              "Y9vWsvw/p3keJdUEqDfFK34HNdJfQtNAUDbQTzj0rJu7sdUVZGbca1aRRs2Thf4QOTVeHxDBNx5Uif71ObRIVXcyZPv0qGS" \
              "yRecDFTKUVoVGMmaUNykwJXmiWRIkLmq1pFj7tSTRFoyDWTaWpp5GbceIUtcbbWWQnstQx+KFkkKG2eM/7QqwIEZ8ECrMdl" \
              "C+BtU/UVPMuw3DrcWzvUu1JI2uOxqHU7Jby1eMjqKsC1SKQNH1FPaspeRUTgNAtxp/j7TC68GYAjHfpX0yv3" \
              "R9K+fHtSfHmliPG4zqf1zX0Gn3B9K7aLvG5xVlaQtFFFbGIUUUUAA6UUDpRQAUHpRUN1IYbWWRRkqpIoBH" \
              "ntzp5sPGmoED5LiMSg++eakupBFEWKk47DqarWt7Nqd5Hfyu37xHTYTnBBHT2rQkQtxisL31R2u" \
              "Lh7r6HGahf69LFO0ECWwUfu1Zdxf6noKx9Nv/ABEyFr+FJBuxsChWx68cfhXoNxGvl4rPSxUvn" \
              "HeolroVG24abHhDv79qsSqmx881MI1hT3qFj1GM5qZqyHHVtnN6jHeRki1wWLcuf4R647msK3s" \
              "vE76ox/tCcWu44YEZx246Zru5bdGUZH0IpLaFUbBA/Koi7IqSUtzF07+14pCl5skGeHAwT9e1bBQ" \
              "5yetXHgG3KioSCM5rOSsO9zN8NWH2/wCIyyP9y0j359yOP517IOleMRxy2t1qF7A7LJldoBwOB1Nes6NNJ" \
              "caRazSnMjxgt9cV1Yeaa5TmxFNr3+5eooorpOUKKKKAAdKKB0FFABTJkEsLoejDFPooA812jTdQTTSOULHP1y" \
              "avu2BkU/xFprprovwSV2YK461AG3IK57WdjvlJStLuRSLubmoHkWI5NWW6VSeLzZMnoKOpJM8sKsiTSojv91SwBNV" \
              "57m2iAMk6x5O0FiACazr7SbS81OK+uYzLNAP3WTwp9frVS/0ay1RP9LiMmDlDn7p9qmexcbdzaeTYApIPoaljC" \
              "uM557VTgh3RhWl3EDFWYwVWsC3YmMu1SKqu/Wnvk1BJ7VMncEVIbpnvJrIqAJWwpxyeK9a06A22nwR" \
              "HqqAV5ha2LXGpWkqk7gwAUCvV0GI1B9K6MMt2Y4uStFIdRRRXWcQUUUUAA6CigdBRQAUUUUAUtRsRf" \
              "W5QEBh0JrlLmyksH8qQhiOcgda7isfXbMzQCZR8y9fpUTjfU1pzto9jlm5FZ81zGjbZJAmeeT1q87b" \
              "QfWsa406C9uVmuE3+XyoPY1jfU6Ul1GTarbqCEZMerHrVAa3Cq/K0e3PTdVy7+x20J3Qg/QVnw3Vu2d" \
              "tuGB6ErjFTNo66cYcpbi1S1lVnjlCSY6E1owT+am7H1rI/sy0uRukgQt2OMVoQfu12+lc7ZElG+haboT" \
              "UllZPqN2tvGwBbue1Vy+e9dT4OsTiS8deD8qf1qqceeSRlUlyRuX9G8Ptp83nTuruOFCjgVv0UV3xio" \
              "qyOCUnJ3YUUUVRIUUUUAA6CigdBRQAUUUUAFIyh1KkZBpaKAOD1aEW1+8f8OeDWc6YBI71u+IQj3pw" \
              "Q3HPtXNTSSW5I5dP1FcstGd0NUhJIUblsEVXKw5ICgVWudTRcjOKzJNWRDkEmspyRtGLN7YB0NMkdUH" \
              "UZrBOukjCIWNNjkurt/nJUHsK52zVQfU3beX7TcJEnO5gCa9bsrdLW0jhjGFVQK8s0KBV1G0j/AOmgr" \
              "1legrswq0bOHFvVIWiiius5AooooAKKKKAAdBRQOgooAKKKKACvL/ih43vNGnh0rTZ0t5ZE3yzt/Avt7" \
              "13et6/ZaJAGuZB5j52Rjq1eBfEe7/trVrC/f91Fd2yvnrgBmB/lSbNIwdlJrQ7HwjcNdeGLed53neRpG" \
              "Mr9WO481qsqucMKzPC6wx+GLFIAAnl5Az6nNaJODwa5nqdaViC50+F1JKA1iS6RCzkiMCt64kbaMNis+" \
              "e48tC2QT2rKolY1p8xTTTIYxkKBU8cKr90Ae9MSVpDljU4Py/1rnsjVtlDWZWg0e6kim8mQJ8sh42nsa7" \
              "L4Y+NJ/Emny2OoDF/Z4Vz/AHx61wXiYq2hXatyDH0NZvwq1qPRdYu9Qut5tViWJm6nJPA9+FP5V14Z2T" \
              "OTEQcmktz6PorN0vXtM1mES2F3FOp/utyPqK0q7Diaa3CiiigQUUUUAA6UVSvNUs9Pi33M6IPc81yGrf" \
              "EOKNWSwi3N2d+n5VLklub0cNVrP3EdzJNHCpaR1VR1JOK5zVPGul2QMcUvny9AI+R+deYX2t32pSl7q4" \
              "d/Rc/KPw6VlPK6szZPqKxlW7Hr0coW9RmfqXiC71jxZJPdyMRlkRSeFHpUlxAdX8DzoBm70SdsjuYJDn" \
              "P4NWHrKG01jz1+65Eqn19a2tE1SLSfE9tcT4awv0Nvcg9CrcZP6H860i/eXmjlr0n7KcOsJfgy54C14e" \
              "QdLnbDxkmInuPSu5Lg968j8Q6TceFfFElsjMAjCS3k/vIeh/ofpXdaDri6naKWwJV4dc96ipGzOenLmRvX" \
              "GTHxyKw5bZ3m3nge5q/PMwBwfwrNkupQ2MD865ajTOqndbFqNQg681IXAHWqqM5XLZrB1/XRZwMkTfv" \
              "Dxms4xbdkVJpK7M7xlrKuP7Pgbdk5kI/QU+6txoek2OktxcmNr289VZhhF/AZ/Oq/hnT4oYZvF" \
              "WsgmytTmCNutxL2x7A/r9KydS1C4u47m/umzdX0m4+y9gPYCuvkUY8i6nPQlz1faPaOv+X3s0f" \
              "CGpXen3E0trM0brggg165ovxOcbYtTh3Y4MkfX8q8f0mA21koYYkk+ZvYVohsd6xlVam3FnsUM" \
              "BCeHjGqtT6K0zxBpurIGtbpGP8Adzgj8K1Mg18zQXcsEgeN2Rgcgg4rsdJ+I+p2IVLjFzGP73X" \
              "862hiV9o4K+TzjrSdz2iiuP0v4iaRfREzubeQDkP0/Oit1Ug+p5ssNWi7OLPM7u/uLuQvNKzk9" \
              "yc1TZs9TSFqME1yXPsoQUVZCrzTHXJpy9aVhzQWZt/Zfb7MwcCaPLRH1HpWNHG13pUlswIngPA" \
              "PUf55FdO6ZxglWHII7Gqctskt0J1xHc42sOiyD/GmpWVjlrYVTnzrqrP0/wCAbCwr8QPASBMH" \
              "XNIG3H8Uien4gfmPeuW8MzutyQuRNHwyHjcKlsdTufCPiOHVIFbyXO2eLpuU9R/Ue9dB410RY" \
              "pIPGnh8h7SbEkyoOFJ/ix6HoR2NdMv3kLo+XnCWGrOEjfjhF1AsidxQmnHdlgKpaLrEF5axzx" \
              "HEcnUZ5Vu4Na8t2kUTOzAKBkkngCuVRu9TpbaWhk61IljYvIzhFUZLGuJ0PRJfFmoy3lyxg0i" \
              "2O6aZjjIHO0H1x1PatFYr34ha99kti0WlW7Zllx29fqewp3irVRdxp4a8Ox+VpVudssqcLIR7" \
              "9x/M1vGChqc8pTqv2cFcy9e1hfEmpR21onlaLY/LBGBgNjjOP88fU1Shtftlz9qlBEEfESf3v" \
              "f6Vet7OG2hEKjzMdVHQ/WrSpzubBI6AdBXPKpd3R9DhcvjTgoy9X5vp8kNC4GT1NIRinmm9awPT" \
              "G9qASKXFIRQJoUMRRTcGigmxrk4qReVooroQgYYPFBNFFAxn1pkiK42sMiiikMheJihjdUnj/uS" \
              "Dn860NG1z+wrOayS3DWU2d9vMCycjBx6Z9KKKak47GVWhSqr34pmBaW50y4mltbgfYpiSI2z8vp" \
              "z3x0q1dXpv7BrOSdyjH5vKHJHpRRUub5rnPHBUIqyjoSWV1d2Gnf2fZboLY5LLkAuT13Y5NQmPI" \
              "+d8/wCyowKKKhyb3OqnShBWgrAeBhRge1KPu0UUjYZTDxRRSEJRjiiigAxRRRQB/9k="

# known_image = face_recognition_util.convert_to_image(base64_code)
b = "iVBORw0KGgoAAAANSUhEUgAAAFoAAABUCAIAAACNwLclAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAABwcSURBVHhe7dtptJbjvwfw88rL//LG8tIL8cLCYq3WQoalZQiJyJQQiZSITSl2kxKVyqxQxjKeItqJQkUyZSjzPGaezzFzPs/9fbrPrv20e57+nRdnrX5rudd1X/d1/Ybvb7h+19P2H/+1mdbQP//8sxmO/6WNhOPXX3+tjgr67rvvqqMN0S+//PL9999XXxqh/y6o+tIuEVEdNU6bIDp+++236mht+umnn6qjTUo///wzQH/88cfqe+GM+v3RPm0kHDzw8ccff/HFFzT78MMP33777c8++4yi1c+t6Pfff4fL6tWr33rrrRUrVixbtmzp0qUPP/zwIwXNnz//gQce+M+CZs+e/eCDDz700EOeaN68eYsWLXr66adfeumld95558svv1wnJNH6PLHR1DAcMY+Ks2bNuvvuuyl9++2333TTTQsWLHjvvfcgAikLUNYbvPvuu4sXL77lllsuueSSCy64oKmpqWfPnieddFKfPn1OOeWUEwsy7tev34ABA84880zPMwo6++yzhw0bNnr0aJA99dRTAaXMBQPKrJNEn3/++euvv/7iiy9++umn1alGaGOig1p33HEHq84555zzzjuvV69e++67b/fu3QcOHDhx4kQwcTvtn332Wc63cvz48T4dccQR++yzz5577mmx50EHHXT88ceffvrp7McHTMOHD588efLll18+btw44/PPP39QQeeee24WjBkzZurUqUKmNFXKSBNx+txzz82ZM2f69OnTpk278cYbQU+Br7/+Osvqp42BQ8xfffXVQ4cO5To+7NKly2677daxY8cdd9xx22233X777Rncv39/KHA4sCDVraAjjzxSFLDz1ltvlQ7PP/+8wPlkDTFSQr322mtCT04tXLhw7ty5991331133UWKgOratevRRx/d3Nx8//33WyY9oSDuLBB31vTt23fIkCETJkywhlfefPPNtvnVPm0MHE888QQ33nbbbZzPXbzHcnFx0UUXHXXUUUDp0KEDRE4++eSED29LKCGjEKxateqjjz6Cgroj2olHf/75pypAdcHvKePi9q+++orNatOSJUvuvffeK6+8EqtLL72UwYJo0qRJ5JIu40gRFPRRembOnMkZ9KFnowGyMXCoeWPHjn388ceZxMKbb76ZftBRIJFXUS2VZL4IorHMB8Hff/9N2B9//MF4Zv/1119eTZpBeUUG67wCyBYAQUdePPPMMzNmzBg8eHDv3r2POeYYAUh6S0uLkqF4vfDCC3AHEN8oz6CsKl0fkdgAHHzIdWKYT+655x7udaaI55EjRxI/ZcqUOOSbb76RCLQRFEosRb/99ttAgECQATJGsbx9sh0ZWC+t4H7NNdeIFFjjbwZMkSWgeEKS0gdAVdXrI/wbiw4nhdQVnFDgRk6TokL0hhtuEL0Kpwr6/vvvK7cvv/yyWkBRCLKcJE9bSlxQ/XBUQuiPPzIWLALzjTfeePLJJwFNJeVGNsFIOKCzzjqrR48eQphuVb3rI8wbg+OHH35Qw1UsKcMe+z11H4znKEcvnZxzojoRwYaYXRhS8S2qIFFQXvNpg7TOYuMcuiLxzjvvFK3qK/VoIpUcZI4nwRK16yRsG4ODkeJCdBCf6I3TZDiP8QZHUcs4WJjXF9C79C2qglE3HK3XpO6iSH/11VeVLW5YuXIlWaSAw0Fz7LHHgkN4VvWujzBsDA71TEVQwDwjHkCspSVeVJQ+XASC2M/mqG4Bq7yaL6CoUIHGhuEot+fVwN7MSA1V44MPPqCMV5PGzh2t3ahRo/7P4SDsqquucog62BlGPOM9aQyU1riYN4jenhU71vi2gkRBDED51D5ZTFygrE4VgUmQ2mHgFSsDp7jjzLnjgBOnYLKmqv2GCJPG4ND5XHzxxQ52h3zEE4YLO30VGvGSSY1DAIpCpfEVGNZQZiqW1UHW4xMiDhmYJDdxao1JJdaJo9/Vekilhi7QODQABz84zDSjWmYniM05NYikEFU8USz0pGIoNhhYU4FhDRVo1JUsFmecLSjzGELc2EDceTpoAaG7dxKDxsHPSVUDNkT41IAD0wxaX5wFvzh0oOqytYA5w6IQO6kCiChEV8/YUKpeDlC2BJ1yshwgG1svCHMUnsggKIQqrNcUFKR/FcKOG0c+E1pb0T5hVW90YO3+et11111xxRVOU06gUGv7aU+h6IdM+krvWFVYUSWTIZ8sy2Lz5bJwK9cQRAGRqEKHp6fJ7G1NZtCjjz562WWXKaiaVLvAUWfK4FAvHPpxkKujbl9CgwySzMd1lEMGMb60x5N50RXF1JJa29N6WUkxL6wChF0VwAoKE4OST9ZLEI28jNYiOfjEtQMxVrRPONQLh6bblcyVRH0iABZKSQ7UktZRrlQ3r8grkyqmFFSdLczwycBklVfBrTpaEynIuJwvX+3CwTOf8OE8BdXN26VR7aizfNi4Xjji/JBwEHvoscceExcEF7n8a0xKXISM03ehMnAMCv0rXRlupWHZHizMWElvVx7ORJyMDMxwMrncYAE3RLeSSRxQImJedjj7KOxKsXr16sjdILUHR0lYa/vEntqhscGaEmUat0aNopSmfYjq9rIkqWujXdYblAQCM3ax/PPPP3f3dS10InCAp0h85ZVXeFgHYcZVSN+l5YULVnjaTofAGgIKiQauS+5Qqr4+Dab1lA+7NgwHJVSN0aNH0yk/z5WqMENjxnIalPa4RzqDkE+ezFOGuSi4xMnGFrONke44Tz31lLh7/PHHHeRqk+sPr7oNsGf69OkKwS233KIPdjPgEonAKxgi+uBJH6Aka5AZTz5zY8h27RKJMacdWi8cTEX4OkHckdzop02bxi08STAizJM2HLhs2TIqMskF36ETe5DexCf3TgMeBpOr3SeffAIyEHO7T27DLh2SXCuJXDfgrr8eOXLk0KFDzzzzzFMK6tOnz2mnnebmPmLEiKlTp9qFMyjxFAU8ITApnID1TICYvOuuu2xx4eSGqm3rp9pw4JsB492IxBuF+Ad3wuyBBaSosnz5cinqhFditT3jxo2TU+7X9Hat1CbriGjPydKNTgsXLgQNM7hLINhoF8sHDBhw0kknuWj07NnzuOOO69Wr1wknnOAa5p7ubupO4PWYY445+uij4aIPdMCVvzBCFiJ0g4L0ZDYlDQSIp69z587lSzG4QUQ2AIf9S5cudYazjdmCPB6AvRTwSfSylj+bmprY061bt3333XePPfbo1KnT3nvvfeihhx511FF9+/b1lQ18rkECzZIlS1paWgymTJnS3NwMPkbC4vDDD2ez9To9GI0dO1a8TJo0Sadjr767e/fuBx98sDUDBw50YcVBPIo7WRlTOYluUJC/iV8Del5//fWcIZZj1/povckSwgu0jBEgqoBggYX6J2uEurwQFEy66KKLhAN7eBIEBx100P777w+XI488koXIPD9zMqtEmY354Vs0nXfeeeCQjMJKpsgaIWMByJKDCiGblQwbOQZS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"
# unknown_image = face_recognition_util.convert_to_image(b)
known_image = cv2.imread("c:/Users/lenovo/Desktop/a3.png")
unknown_image = cv2.imread("c:/Users/lenovo/Desktop/a3.png")
result = face_recognition_util.contrast_faces(known_image, unknown_image)
with open("c:/Users/lenovo/Desktop/ad.jpg", "rb") as a:
    base64_data = base64.b64encode(a.read())
end_time = datetime.now()
print("识别人脸完成,识别用时：{}秒".format((end_time - start_time).seconds))
if result:
    print("same person")
elif result is None:
    print("recognition error")
else:
    print("not same person")

faces_position = [
    "D:/facedected/candidate-faces/girl1.jpg",
    "D:/facedected/candidate-faces/girl2.jpg",
    "D:/facedected/candidate-faces/girl3.jpg",
    "D:/facedected/candidate-faces/girl4.jpg",
    "D:/facedected/candidate-faces/girl5.jpg",
    "D:/facedected/candidate-faces/girl6.jpg",
    "C:/Users/lenovo/Desktop/f703738da9773912f6290861f3198618367ae2a7.jpg",
    "C:/Users/lenovo/Desktop/timg.jpg",
    "C:/Users/lenovo/Desktop/lfy.jpg"
]
known_face_encodings = []
for position in faces_position:
    image = cv2.imread(position)
    face_encoding = face_recognition_util.get_face_encoding(image)[0]
    known_face_encodings.append(face_encoding)

known_face_names = [
    "未知1",
    "未知2",
    "刘诗诗",
    "范冰冰",
    "刘亦菲",
    "任吴昊",
    "奥巴马",
    "特朗普",
    "罗福勇"
]
face_recognition_util.real_time_comparison(known_face_encodings, known_face_names)
