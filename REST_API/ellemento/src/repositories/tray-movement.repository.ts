import {inject, Getter} from '@loopback/core';
import {DefaultCrudRepository, repository, HasManyRepositoryFactory} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {TrayMovement, TrayMovementRelations, History} from '../models';
import {HistoryRepository} from './history.repository';

export class TrayMovementRepository extends DefaultCrudRepository<
  TrayMovement,
  typeof TrayMovement.prototype.tray_movement_id,
  TrayMovementRelations
> {

  public readonly histories: HasManyRepositoryFactory<History, typeof TrayMovement.prototype.tray_movement_id>;

  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource, @repository.getter('HistoryRepository') protected historyRepositoryGetter: Getter<HistoryRepository>,
  ) {
    super(TrayMovement, dataSource);
    this.histories = this.createHasManyRepositoryFactoryFor('histories', historyRepositoryGetter,);
    this.registerInclusionResolver('histories', this.histories.inclusionResolver);
  }
}
