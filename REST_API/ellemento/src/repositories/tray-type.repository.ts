import {inject, Getter} from '@loopback/core';
import {DefaultCrudRepository, repository, HasManyRepositoryFactory} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {TrayType, TrayTypeRelations, Stage} from '../models';
import {StageRepository} from './stage.repository';

export class TrayTypeRepository extends DefaultCrudRepository<
  TrayType,
  typeof TrayType.prototype.tray_type_id,
  TrayTypeRelations
> {

  public readonly stages: HasManyRepositoryFactory<Stage, typeof TrayType.prototype.tray_type_id>;

  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource, @repository.getter('StageRepository') protected stageRepositoryGetter: Getter<StageRepository>,
  ) {
    super(TrayType, dataSource);
    this.stages = this.createHasManyRepositoryFactoryFor('stages', stageRepositoryGetter,);
    this.registerInclusionResolver('stages', this.stages.inclusionResolver);
  }
}
