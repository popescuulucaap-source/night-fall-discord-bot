# FadeHost launcher for the modular Nightfall build.
import main
import nightfall_upgrades

nightfall_upgrades.install(main)
main.bot.run(main.TOKEN)
