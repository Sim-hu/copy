def create_skill_command(skill_name):
    @tree.command(name=f"skill_{skill_name}", description=f"{skill_name}の詳細を表示します")
    async def skill_command(interaction: discord.Interaction):
        await interaction.response.send_message(get_skill_info(skill_name))
    
    return skill_command

# スキルコマンドを作成する例
create_skill_command("火球")
create_skill_command("回復")
create_skill_command("氷結")
