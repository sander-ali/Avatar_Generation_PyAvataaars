#First install py-avataaars using pip install py-avataaars
#Install the gtk file from the link: https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer
#I used  gtk3-runtime-3.24.29-2021-04-29-ts-win64.exe

#import the package
import py_avataaars as pa

#assign parameters to your avatar
avatar = pa.PyAvataaar(style = pa.AvatarStyle.CIRCLE, 
                       skin_color = pa.SkinColor.LIGHT,
                       hair_color = pa.HairColor.BROWN_DARK,
                       top_type = pa.TopType.SHORT_HAIR_SHORT_FLAT,
                       mouth_type= pa.MouthType.SMILE,
                       eye_type = pa.EyesType.SQUINT,
                       eyebrow_type = pa.EyebrowType.DEFAULT,
                       nose_type = pa.NoseType.DEFAULT,
                       accessories_type = pa.AccessoriesType.PRESCRIPTION_02,
                       clothe_type = pa.ClotheType.HOODIE,
                       clothe_color = pa.Color.BLACK,
                       clothe_graphic_type = pa.ClotheGraphicType.BAT)

avatar.render_png_file("SAK_AVATAR.png")
                       